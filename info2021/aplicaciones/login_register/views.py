from .models import Usuario
from .forms import UsuarioForm
from django.shortcuts import redirect, render


#from django.http import HttpResponse
#import datetime

# Create your views here.

def home(request):
    return render(request, 'index.html')



def crearUsuarios(request):
    if request.method == 'POST':
        nuevo_registro = UsuarioForm(request.POST)
        if nuevo_registro.is_valid():
            nuevo_registro.save()
            return redirect('index')
    else:
        nuevo_registro = UsuarioForm()
    return render(request, 'login_register/crear_usuario.html', {'nuevo_registro': nuevo_registro})




def listarUsuarios(request):
    usuarios = Usuario.objects.all()
    return render(request, 'login_register/listarUsuarios.html', {'usuarios':usuarios})