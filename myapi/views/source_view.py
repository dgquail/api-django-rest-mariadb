from rest_framework import generics, permissions, viewsets
from ..models import Source
from ..serializers import SourceSerializer

class SourceListCreateView(generics.ListCreateAPIView):
    """
    Endpoint para listar y crear.
    """
    queryset =Source.objects.all()
    serializer_class = SourceSerializer


class SourceDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    Endpoint para recuperar, actualizar o eliminar.
    """
    queryset = Source.objects.all()
    serializer_class = SourceSerializer

class SourceViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Source.objects.all().order_by('-created_at')
    serializer_class = SourceSerializer
    permission_classes = [permissions.IsAuthenticated]
