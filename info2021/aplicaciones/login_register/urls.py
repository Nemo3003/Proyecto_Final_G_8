from django.urls import path
from .views import Registrarse, equipoView

urlpatterns = [
    path('signup/',Registrarse.as_view() , name='registrarse'),
    path('equipo/',equipoView , name='equipo'),
]

 