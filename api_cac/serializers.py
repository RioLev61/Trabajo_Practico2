from rest_framework import serializers
from cac.models import Proyecto


class ProyectoSerializer(serializers.ModelSerializer):
    class Meta:
        model= Proyecto
        fields= ['id','nombrep','imagenp', 'website']


