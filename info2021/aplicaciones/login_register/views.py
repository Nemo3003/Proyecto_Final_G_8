from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic



#----------------------------------- CREAMOS USUARIOS (NO STAFF) -------------------------------------------------
class Registrarse (generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('home')
    template_name = 'registration/registrarse.html'
#----------------------------------- CAMBIO DE CONTRASEÑAS PARA USUARIOS -------------------------------------------------

     

