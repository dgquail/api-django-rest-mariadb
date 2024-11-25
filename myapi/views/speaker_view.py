from rest_framework import generics
from ..models import Speaker
from ..serializers import SpeakerSerializer

class SpeakerListCreateView(generics.ListCreateAPIView):
    """
    Endpoint para listar y crear.
    """
    queryset =Speaker.objects.all()
    serializer_class = SpeakerSerializer


class SpeakerDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    Endpoint para recuperar, actualizar o eliminar.
    """
    queryset = Speaker.objects.all()
    serializer_class = SpeakerSerializer
