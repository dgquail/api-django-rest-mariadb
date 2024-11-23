FROM python:3.10-slim

# Instalar dependencias del sistema
RUN apt-get update && apt-get install -y \
    gcc \
    default-libmysqlclient-dev \
    pkg-config \
    && apt-get clean

# Configurar el directorio de trabajo
WORKDIR /app

# Copiar y instalar las dependencias de Python
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copiar el resto del proyecto
COPY . /app/

# Exponer el puerto
EXPOSE 80

# Comando por defecto
CMD ["python", "manage.py", "runserver", "0.0.0.0:80"]
