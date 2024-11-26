import tweepy
import base64
from io import BytesIO
from datetime import datetime
from dotenv import load_dotenv
import os


class XHandler:
    def __init__(self):
        """
        Inicializa la conexión con la API de X (anteriormente Twitter) usando Tweepy.
        Carga las credenciales desde un archivo .env.
        """
        # Cargar las variables de entorno desde el archivo .env
        load_dotenv()

        api_key = os.getenv("X_API_KEY")
        api_secret = os.getenv("X_API_SECRET")
        access_token = os.getenv("X_ACCESS_TOKEN")
        access_secret = os.getenv("X_ACCESS_SECRET")

        if not all([api_key, api_secret, access_token, access_secret]):
            raise ValueError("Faltan credenciales en el archivo .env")

        self.auth = tweepy.OAuth1UserHandler(api_key, api_secret, access_token, access_secret)
        self.api = tweepy.API(self.auth)

    def get_following(self, username, count=100):
        """
        Lista los usuarios que el usuario especificado está siguiendo.
        
        :param username: Nombre de usuario (screen_name) de la cuenta.
        :param count: Número máximo de usuarios a listar.
        :return: Lista de diccionarios con información básica de los usuarios.
        """
        try:
            following = self.api.get_friends(screen_name=username, count=count)
            return [
                {"id": user.id_str, "screen_name": user.screen_name, "name": user.name}
                for user in following
            ]
        except SystemError as e:
            print(f"Error al obtener la lista de usuarios seguidos: {e}")
            return []

    def get_tweets_by_user(self, user_id, start_date, end_date, max_tweets=200):
        """
        Obtiene los tweets de un usuario en un rango de fechas.
        
        :param user_id: ID del usuario del que se quieren obtener los tweets.
        :param start_date: Fecha de inicio (formato 'YYYY-MM-DD').
        :param end_date: Fecha de fin (formato 'YYYY-MM-DD').
        :param max_tweets: Número máximo de tweets a recuperar.
        :return: Lista de tweets (diccionarios con contenido y metadatos).
        """
        try:
            start_date = datetime.strptime(start_date, "%Y-%m-%d")
            end_date = datetime.strptime(end_date, "%Y-%m-%d")

            tweets = tweepy.Cursor(
                self.api.user_timeline,
                user_id=user_id,
                tweet_mode="extended",
                count=100
            ).items(max_tweets)

            filtered_tweets = []
            for tweet in tweets:
                tweet_date = tweet.created_at
                if start_date <= tweet_date <= end_date:
                    filtered_tweets.append({
                        "id": tweet.id_str,
                        "text": tweet.full_text,
                        "created_at": tweet.created_at,
                        "user": tweet.user.screen_name
                    })

            return filtered_tweets
        except tweepy.TweepError as e:
            print(f"Error al obtener los tweets del usuario: {e}")
            return []

    def post_tweet_with_image_base64(self, text, image_base64):
        """
        Publica un tweet con una imagen en formato base64 adjunta.
        
        :param text: El contenido del tweet.
        :param image_base64: Cadena codificada en base64 de la imagen.
        :return: Información del tweet publicado o un mensaje de error.
        """
        try:
            # Decodificar la imagen base64 y convertirla a un archivo en memoria
            image_data = base64.b64decode(image_base64)
            image = BytesIO(image_data)

            # Subir la imagen a X (Twitter)
            uploaded_media = self.api.media_upload(filename="temp.jpg", file=image)

            # Publicar el tweet con la imagen
            tweet = self.api.update_status(status=text, media_ids=[uploaded_media.media_id_string])
            return {
                "id": tweet.id_str,
                "text": tweet.text,
                "created_at": tweet.created_at
            }
        except tweepy.TweepError as e:
            print(f"Error al publicar el tweet con imagen: {e}")
            return {"error": str(e)}


# Ejemplo de uso
if __name__ == "__main__":
    # Inicializa la clase
    x_handler = XHandler()

    # Publicar un tweet con una imagen en base64
    base64_image = "<tu_imagen_base64_aqui>"  # Sustituir por tu cadena base64
    tweet_result = x_handler.post_tweet_with_image_base64(
        text="Hello from XHandler with base64 image! 🚀",
        image_base64=base64_image
    )
    print(f"Resultado del tweet: {tweet_result}")
