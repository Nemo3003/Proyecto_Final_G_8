from django.db import models

from participante.models import Participante

class Pregunta(models.Model):
   pregunta_name = models.CharField(max_length=50)
   pregunta_number = models.PositiveIntegerField()
   total_marcas = models.PositiveIntegerField()
   def __str__(self):
        return self.pregunta_name

class Participante(models.Model):
    usuario = models.CharField(max_length=10)
    email = models.CharField(max_length=200)
    password1 = models.CharField(label="Password", strip=False)

class Respuesta(models.Model):
    respuesta=models.ForeignKey(Pregunta,on_delete=models.CASCADE)
    pregunta=models.CharField(max_length=600)
    opcion1=models.CharField(max_length=200)
    opcion2=models.CharField(max_length=200)
    opcion3=models.CharField(max_length=200)
    opcion4=models.CharField(max_length=200)

class Resultado(models.Model):
    participante = models.ForeignKey(Participante,on_delete=models.CASCADE)
    quiz = models.ForeignKey(Pregunta,on_delete=models.CASCADE)
    fecha = models.DateTimeField(auto_now=True)
