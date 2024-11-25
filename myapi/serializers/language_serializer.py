from rest_framework import serializers
from ..models import Language

class LanguageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Language
        fields = '__all__'  # Puedes especificar los campos explícitamente si es necesario
