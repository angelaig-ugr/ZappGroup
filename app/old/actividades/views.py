from django.shortcuts import render
from django.http import HttpResponseRedirect
import datetime

from actividades.models import *
from actividades.forms import *
# Create your views here.


def index(request):
    return HttpResponseRedirect('/actividades/index.html')

# @login_required
def eliminarActividad(request, id):
    Actividad.objects.get(pk=id).delete()
    return HttpResponseRedirect('/actividades') # Hace falta la url

def nuevaActividad(request):
    if request.method == "POST":
        form = nuevaActividadForm(request.POST, request.FILES)
        if form.is_valid():
            dt = datetime.datetime.now()
            form.instance.fechaCreacion = datetime.date(dt.year, dt.day, dt.month)
            form.save()
            return HttpResponseRedirect('/actividades')
    else:
        form = nuevaActividadForm()

    return render(request, 'actividades/nuevaActividad.html', {'form': form})

def modificarActividad(request, id):
    activ = Actividad.objects.get(pk=id)

    if request.method == "POST":
        form = modificarActividad(request.POST, request.FILES)
        if form.is_valid():
            form = form.cleaned_data

            if form['idUsuario']:
                activ.idUsuario = form['idUsuario']
            if form['idProfesional']:
                activ.idProfesional = form['idProfesional']
            if form['video']:
                activ.video = form['video']
            # Falta imagen
            if form['pdf']:
                activ.pdf = form['pdf']
            if form['comentario']:
                activ.comentario = form['comentario']
            
            activ.save()

            return HttpResponseRedirect(request.build_absolute_uri())
    else:
        form = modificarActividad(instance=activ)
    return render(request, 'gestion_tareas/modificar_tarea_cuidado.html', {'form': form})


def verActividad(request, id):
    actividad = Actividad.objects.get(pk=id)
    context = {'actividad': actividad}
    return render(request, 'actividades/verActividad.html', context)

# Esto habrá que mirar que lo esté mirando un usuario
def verActividadesRealizadas(request, id):
    actividad = Actividad.objects.get(idUsuario=id, estado=ENTREGADO)
    context = {'actividad': actividad}
    return render(request, 'actividades/verActividadesRealizadas.html', context)

def verActividadesUsuario(request, id):
    actividad = Actividad.objects.get(idUsuario=id)
    context = {'actividad': actividad}
    return render(request, 'actividades/verActividadesUsuario.html', context)
