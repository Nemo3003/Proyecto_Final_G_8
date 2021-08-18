from django.shortcuts import render, redirect, HttpResponse

from .models import perfilUsuario, Pregunta

from django.template import loader  

from django.shortcuts import render  
# Create your views here.
def inicio(request):
    context = {
        'bienvenido': 'Bienvenido'

    }
    return render(request, 'inicio.html', context)

def homeUsuario(request):

    return render(request, 'login_register/home.html')

def jugar(request):

    quiz_usuario, created = perfilUsuario.objects.get_or_create(usuario=request.user)
    
    if request.method == 'POST':
        pregunta_pk = request.POST.get('pregunta_pk')
        correcta = quiz_usuario.intentos.select_related('pregunta').get(pregunta_pk = pregunta_pk)
        respuesta_pk = request.POST.get('respuesta_pk')
    else:
        pregunta = Pregunta.objects.all()

        context = {
            'pregunta': pregunta

        }

    return render(request, 'play/jugar.html', context)

def loginView(request):
        return redirect('homeUsuario')