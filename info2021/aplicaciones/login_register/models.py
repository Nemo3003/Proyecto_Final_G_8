from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Equipo(models.Model):
    id_usuario = models.ForeignKey (User, on_delete=models.CASCADE)
    descripcion_personal = models.TextField(max_length=500, blank=False, null=False)
    imagen = models.ImageField(upload_to='login_register')
    funcion = models.CharField(max_length=100, blank=False, null=False)
    facebook = models.URLField()
    instagram = models.URLField()
    twitter = models.URLField()

    def __str__(self):
        x = self.id_usuario.username
        return x

    class META:
        verbose_name = "Equipo"
        verbose_name_plural = "Equipos"    



