from rest_framework import generics
from ..models import Config
from ..serializers import ConfigSerializer

class ConfigListCreateView(generics.ListCreateAPIView):
    """
    Endpoint para listar y crear
    """
    queryset = Config.objects.all()
    serializer_class = ConfigSerializer


class ConfigDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    Endpoint para recuperar, actualizar o eliminar
    """
    queryset = Config.objects.all()
    serializer_class = ConfigSerializer
