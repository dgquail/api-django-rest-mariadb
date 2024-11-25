from rest_framework import generics
from ..models import Speech
from ..serializers import SpeechSerializer

class SpeechListCreateView(generics.ListCreateAPIView):
    """
    Endpoint para listar y crear discursos.
    """
    queryset = Speech.objects.all()
    serializer_class = SpeechSerializer


class SpeechDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    Endpoint para recuperar, actualizar o eliminar un discurso.
    """
    queryset = Speech.objects.all()
    serializer_class = SpeechSerializer
