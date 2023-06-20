from django.urls import path
from .views import Home,crearAutor

urlpatterns = [
    path('',Home,name='index'),
    #path('crear_autor/',crearautor, name='crear_autor')
    path('crear_autor/', crearAutor,name='crear_autor')
]
