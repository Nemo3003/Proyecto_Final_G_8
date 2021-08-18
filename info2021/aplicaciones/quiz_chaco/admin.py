from django.contrib import admin
from .models import Pregunta, Respuesta, Intentos_respuesta, perfilUsuario
from .forms import ElegirInlineFormset

class RespuestaInline(admin.TabularInline):
    model = Respuesta
    can_delete = False
    max_num = Respuesta.maximo_elecciones
    min_num = Respuesta.minimo_elecciones
    formset = ElegirInlineFormset

class PreguntaAdmin(admin.ModelAdmin):
    model = Pregunta
    inlines = (RespuestaInline, )
    list_display = ["titulo", ]
    search_fields = ['titulo', 'pregunta__texto']


class Intentos_respuestaAdmin(admin.ModelAdmin):
    list_display = ["pregunta", "respuesta","correcta","puntaje"]
    
    class Meta:
        model = Intentos_respuesta
admin.site.register(Pregunta, PreguntaAdmin)
admin.site.register(Respuesta)
admin.site.register(Intentos_respuesta)
admin.site.register(perfilUsuario)
