from rest_framework import generics
from ..models import Language
from ..serializers import LanguageSerializer

class LanguageListCreateView(generics.ListCreateAPIView):
    """
    Endpoint para listar y crear.
    """
    queryset =Language.objects.all()
    serializer_class = LanguageSerializer


class LanguageDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    Endpoint para recuperar, actualizar o eliminar.
    """
    queryset = Language.objects.all()
    serializer_class = LanguageSerializer
