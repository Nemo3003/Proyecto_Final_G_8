from django.urls import path

from .views import inicio, jugar

urlpatterns = [
    path('', inicio, name='inicio'),
    path('jugar/', jugar, name='jugar'),
]