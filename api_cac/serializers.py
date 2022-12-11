from rest_framework import serializers
from cac.models import Proyecto, Posteo


class ProyectoSerializer(serializers.ModelSerializer):
    class Meta:
        model= Proyecto
        fields= ['id','nombrep','imagenp', 'website']


class PosteoSerializer(serializers.ModelSerializer):
    class Meta:
        model= Posteo
        fields= ['id','titulo','resumen', 'articulo','imagenpos','fecha']


