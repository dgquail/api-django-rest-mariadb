from rest_framework import serializers
from ..models import Source

class SourceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Source
        fields = '__all__'  # Puedes especificar los campos explícitamente si es necesario
