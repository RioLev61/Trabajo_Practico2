from rest_framework import viewsets
from rest_framework import permissions
from cac.models import Proyecto, Usuario
from api_cac import serializers



# Create your views here.
class ProyectoViewSet(viewsets.ModelViewSet):
    queryset = Proyecto.objects.all().order_by('id')
    serializer_class = serializers.ProyectoSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all().order_by('id')
    serializer_class = serializers.UsuarioSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

