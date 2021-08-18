from django.db import models
from django.conf import settings

from django.contrib.auth.models import User
#from login_register.models import Usuario
# Create your models here.

class Pregunta(models.Model):

    numero_respuestas_disponibles = 1
    titulo = models.TextField(verbose_name="texto de pregunta", null=True)

    def __str__(self):
            if self.titulo==None:
                return "No title found"
            return self.titulo

class Respuesta(models.Model):
    
    maximo_elecciones = 4
    minimo_elecciones = 2

    pregunta = models.ForeignKey(Pregunta, related_name="pregunta", on_delete=models.CASCADE)
    correcta = models.BooleanField(verbose_name = "¿Es esta la pregunta correcta?", default=False, null=False)
    titulo = models.TextField(verbose_name = "Texto de la respuesta")

    def __str__(self):
        return self.titulo

class perfilUsuario(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    puntaje_total = models.DecimalField(verbose_name="Puntaje total", default=0, decimal_places=2, max_digits=10)

class Intentos_respuesta(models.Model):
    usuario = models.ForeignKey(perfilUsuario, on_delete=models.CASCADE)
    pregunta = models.ForeignKey(Pregunta, on_delete=models.CASCADE)
    respuesta = models.ForeignKey(Respuesta, on_delete=models.CASCADE, related_name="intentos")
    correcta = models.BooleanField(verbose_name = "¿Es la respuesta correcta?", default = False, null = False)
    puntaje = models.DecimalField(verbose_name="puntaje obtenido", default=0, decimal_places=2, max_digits=6)


