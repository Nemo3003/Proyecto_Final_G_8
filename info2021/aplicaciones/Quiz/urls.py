from django.urls import path
from .views import (
			HomeUsuario,
			team,
			jugar,
			resultado_pregunta,
			tablero,)
#Powered by Nemo with help from Google
urlpatterns = [
	path('HomeUsuario/', HomeUsuario, name='HomeUsuario'),
	path('Team/index.html/', team, name='team'),

	path('tablero/', tablero, name='tablero'),  
#Powered by Nemo with help from Google
	path('jugar/', jugar, name='jugar'),
	path('resultado/<int:pregunta_respondida_pk>/', resultado_pregunta, name='resultado'),
]
