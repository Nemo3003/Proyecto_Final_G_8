from django.db import models


# Create your models here.

class Usuario(models.Model):
    id_usuario = models.AutoField (primary_key=True)
    nombres = models.CharField(max_length=35)
    apellidos = models.CharField(max_length=35)
    usuario = models.CharField("usuario", max_length=25, null=False, blank=False)
    contraseña = models.CharField("contraseña", max_length=12, blank=False, null= False)
    creado = models.DateField("creado", auto_now= False ,auto_now_add=True)
    email = models.EmailField("email", blank=False, null=False)
    estado = models.BooleanField("estado", default=True)
    
    def __str__(self):
        if self.estado:
            y = "ACTIVO"
        else:
            y = "INACTIVO"
        
        x = f"{self.usuario} ---> {y}"
        return  x

    class META:
        verbose_name = "Usuario"
        verbose_name_plural = "Usuarios"
        ordening = ("nombres")    

