from django.shortcuts import render, redirect, HttpResponse

from .models import perfilUsuario, Pregunta, Intentos_respuesta

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
    quiz_usuario, created = perfilUsuario.objects.get_or_create(usuario=request.user)
    
    if request.method == 'POST':
        pregunta_pk = request.POST.get('pregunta_pk')
        pregunta_respondida = quiz_usuario.intentos.select_related('pregunta').get(pregunta__pk = pregunta_pk)
        respuesta_pk = request.POST.get('respuesta_pk')
    else:
        #De esta manera si una pregunta es respondida correctamente, se la elimina. 
        #Esto tiene la ventaja de que solo hay un intento permitido
        #Flat: Se usa para regresar un queryset de valores unicos en lugar de una tupla
        respondidas = Intentos_respuesta.objects.filter(Quiz_usuario=quiz_usuario).values_list('pregunta__pk', flat=True)
        pregunta = Pregunta.objects.exclude(pk__in=respondidas)

        context = {
            'pregunta': pregunta

        }

    return render(request, 'jugar.html', context)

def loginView(request):
        return redirect('homeUsuario')