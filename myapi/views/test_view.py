from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from ..models.expert.x_handler import XHandler

class CustomEndpoint(APIView):
    def get(self, request, *args, **kwargs):
        # Lógica para solicitudes GET
        data = {"message": "This is a GET request"}
        return Response(data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        # Lógica para solicitudes POST
        #received_data = request.data
        #response_data = {"message": "Data received", "data": received_data}

        x_handler = XHandler()
        folowings = x_handler.get_following(x_handler,'dgquailarg')
        response_data = {"message": "Data received", "data": folowings}

        return Response(response_data, status=status.HTTP_201_CREATED)
