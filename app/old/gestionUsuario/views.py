from django.shortcuts import render

from gestionUsuario.models import *

# Create your views here.


def verPerfil(request, idUsuario):
    usuario = Us.objects.get(id=idUsuario)
    context = {'perfil': perfil}
    return render(request, 'perfil.html', context)

def crearUsuario(request, n_nombre, n_email, n_coordinador, n_edad):
    Usuario.objects.create(nombre = n_nombre,
                email=n_email,
                coordinador=n_coodinador,
                edad = n_edad)
