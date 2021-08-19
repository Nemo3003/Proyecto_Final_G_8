from django.core.exceptions import ObjectDoesNotExist
from django.http.response import Http404
from django.shortcuts import render, redirect, HttpResponse

from .models import QuizUsuario, Pregunta, PreguntasRespondidas

from django.template import loader  

from django.shortcuts import render  
# Create your views here.
def inicio(request):
    context = {
        'bienvenido': 'Bienvenido'

    }
    return render(request, 'inicio.html', context)


def jugar(request):
    #ESto crea un usuario en el "jugar"
    QuizUser, created = QuizUsuario.objects.get_or_create(usuario=request.user)
    
    if request.method == 'POST':
        pregunta_pk = request.POST.get('pregunta_pk')
        pregunta_respondida = QuizUser.intentos.select_related('pregunta').filter(pregunta__pk = pregunta_pk)
        respuesta_pk = request.POST.get('respuesta_pk')
        
        try:
            opcion_seleccionada = pregunta_respondida.pregunta.opciones.filter(pk=respuesta_pk)

        except ObjectDoesNotExist:
            return Http404
        
        QuizUser.validar_intento(pregunta_respondida, opcion_seleccionada)

        return redirect(pregunta_respondida)
    else:
        #De esta manera si una pregunta es respondida correctamente, se la elimina. 
        #Esto tiene la ventaja de que se permite solo un intento
        #Flat: Se usa para regresar un queryset de valores unicos en lugar de una tupla
        pregunta = QuizUser.obtener_nuevas_preguntas()
        if pregunta is not None:
            QuizUser.crear_intentos(pregunta)
        
        context = {
            'pregunta': pregunta

        }

    return render(request, 'templates/jugar.html', context)

def loginView(request):
        return redirect('home')