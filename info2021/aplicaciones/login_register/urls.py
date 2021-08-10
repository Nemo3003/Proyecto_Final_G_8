from django.urls import path
from .views import crearUsuarios, listarUsuarios

urlpatterns = [
    path('registrarse/', crearUsuarios, name='nuevo_registro'),
    path('usuarios/', listarUsuarios, name='usuarios'),
]
