from rest_framework import serializers
from ..models import Speaker

class SpeakerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Speaker
        fields = '__all__'  # Puedes especificar los campos explícitamente si es necesario
