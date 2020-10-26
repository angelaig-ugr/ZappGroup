from django.shortcuts import render

from gestionUsuario.models import *

# Create your views here.


def verPerfil(request, idUsuario):
    usuario = Usuario.objects.get(id=idUsuario)
    context = {'perfil': perfil}
    return render(request, 'perfil.html', context)

def crearUsuario(request, nuevo_nombre, nuevo_email, nuevo_coordinador, nuevo_edad):
    Usuario.objects.create(nombre = nuevo_nombre,
                email=nuevo_email,
                coordinador=nuevo_coodinador,
                edad = nueva_edad)
