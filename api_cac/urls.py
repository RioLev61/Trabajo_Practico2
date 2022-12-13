from django.urls import path, include
from rest_framework.routers import DefaultRouter
from api_cac import views

router = DefaultRouter()
router.register(r'proyectos', views.ProyectoViewSet, basename='proyecto')
router.register(r'usuarios', views.UsuarioViewSet, basename='usuario')

urlpatterns = [
    path('', include(router.urls)),   
    path('api-auth', include('rest_framework.urls', namespace='rest_framework'))
]