from rest_framework import serializers
from ..models import Config

class ConfigSerializer(serializers.ModelSerializer):
    class Meta:
        model = Config
        fields = '__all__'  # Puedes especificar los campos explícitamente si es necesario
