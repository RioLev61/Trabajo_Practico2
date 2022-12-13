from rest_framework import serializers
from cac.models import Proyecto, Usuario


class ProyectoSerializer(serializers.ModelSerializer):
    class Meta:
        model= Proyecto
        fields= ['id','nombrep','imagenp', 'website']


class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model= Usuario
        fields= ['id','nombre','apellido', 'username','email','password']


