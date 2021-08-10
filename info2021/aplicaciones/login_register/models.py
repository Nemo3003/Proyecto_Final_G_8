from django.db import models
from django.db.models.fields.related import ForeignKey

# Create your models here.

class Usuario(models.Model):
    id_usuario = models.AutoField (primary_key=True)
    nombres = models.CharField(max_length=35, null=False, blank=False)
    apellidos = models.CharField(max_length=35, null=False, blank=False)
    usuario = models.CharField("nombre usuario", max_length=25, null=False, blank=False)
    creado = models.DateField("fecha creación de usuario", auto_now= False ,auto_now_add=True)
    
    def __str__(self):
        x = f"{self.nombres} {self.apellidos}, es {self.usuario}"
        return  x

    class META:
        verbose_name = "Usuario"
        verbose_name_plural = "Usuarios"
        ordening = ("usuario")    



