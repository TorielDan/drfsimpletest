from rest_framework import serializers #Esta biblo es extensión de Framework Django
#que proporciona herramientas y utilidades adicionales para contruir APIs web
from .models import Proyect

class ProyectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Proyect
        fields = ('id', 'title', 'description', 'technology', 'created_at')
        read_only_fields = ('created_at',)