from django.urls import path

from .views import jugar

urlpatterns = [
    #path('', inicio, name='home'),
    path('', jugar, name='jugar'),
]