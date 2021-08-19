from django.db import models
from django.conf import settings

from django.contrib.auth.models import User


import random
# Create your models here.

class Pregunta(models.Model):
    
    numero_respuestas_disponibles = 1
    titulo = models.TextField(verbose_name="texto de pregunta", null=True)
    max_puntaje = models.DecimalField(verbose_name="Maximo Puntaje", default=3, decimal_places=2, max_digits=6)

    def __str__(self):
            if self.titulo==None:
                return "No title found"
            return self.titulo

class ElegirRespuesta(models.Model):
    
    maximo_elecciones = 4
    minimo_elecciones = 2
  
    pregunta = models.ForeignKey(Pregunta, related_name="opciones", on_delete=models.CASCADE)
    correcta = models.BooleanField(verbose_name = "¿Es esta la pregunta correcta?", default=False, null=True)
    titulo = models.TextField(verbose_name = "Texto de la respuesta")

    def __str__(self):
        return self.titulo

class QuizUsuario(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    puntaje_total = models.DecimalField(verbose_name="Puntaje total", default=0, decimal_places=2, max_digits=10)
    
    def crear_intentos(self, pregunta):
        intento = PreguntasRespondidas(pregunta=pregunta, quizUser=self)
        intento.save()

    def obtener_nuevas_preguntas(self):
        respondidas = PreguntasRespondidas.objects.filter(quizUser=self).values_list("pregunta__pk", flat=True)
        preguntas_restantes = Pregunta.objects.exclude(pk__in=respondidas)
        if not preguntas_restantes.exists():
            return None
        return random.choice(preguntas_restantes)
    
    def validar_intento(self, pregunta_respondida, respuesta_seleccionada):
        if pregunta_respondida.pregunta_id != respuesta_seleccionada.pregunta_id:
            return 

        pregunta_respondida,respuesta_seleccionada = respuesta_seleccionada
        if respuesta_seleccionada.correcta is True:
            pregunta_respondida.correcta = True
            pregunta_respondida.puntaje_obtenido = respuesta_seleccionada.pregunta.max_puntaje
        
            pregunta_respondida.save()

class PreguntasRespondidas(models.Model):
    quizUser= models.ForeignKey(QuizUsuario, on_delete=models.CASCADE)
    pregunta = models.ForeignKey(Pregunta, on_delete=models.CASCADE)
    respuesta = models.ForeignKey(ElegirRespuesta, on_delete=models.CASCADE, related_name="intentos", null=True)
    correcta = models.BooleanField(verbose_name = "¿Es la respuesta correcta?", default = False)
    puntaje_obtenido = models.DecimalField(verbose_name="puntaje obtenido", default=0, decimal_places=2, max_digits=6)


