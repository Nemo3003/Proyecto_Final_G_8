from django.contrib import admin
from .models import Pregunta, ElegirRespuesta, PreguntasRespondidas, QuizUsuario
from .forms import ElegirInlineFormset

class RespuestaInline(admin.TabularInline):
    model = ElegirRespuesta
    can_delete = False
    max_num = ElegirRespuesta.maximo_elecciones
    min_num = ElegirRespuesta.minimo_elecciones
    formset = ElegirInlineFormset

class PreguntaAdmin(admin.ModelAdmin):
    model = Pregunta
    inlines = (RespuestaInline, )
    list_display = ["titulo", ]
    search_fields = ['titulo', 'pregunta__texto']


class Intentos_respuestaAdmin(admin.ModelAdmin):
    list_display = ["pregunta", "respuesta","correcta","puntaje"]
    
    class Meta:
        model = PreguntasRespondidas
admin.site.register(Pregunta, PreguntaAdmin)
admin.site.register(ElegirRespuesta)
admin.site.register(PreguntasRespondidas)
admin.site.register(QuizUsuario)
