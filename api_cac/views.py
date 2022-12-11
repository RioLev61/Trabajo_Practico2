from rest_framework import viewsets
from rest_framework import permissions
from cac.models import Proyecto
from api_cac import serializers



# Create your views here.
class ProyectoViewSet(viewsets.ModelViewSet):
    queryset = Proyecto.objects.all().order_by('id')
    serializer_class = serializers.ProyectoSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

