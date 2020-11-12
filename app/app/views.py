from django.shortcuts import render
from django.http import HttpResponseRedirect
import datetime

from app.forms import *
# Create your views here.

#imports de serialziers
from .serializers import *
from rest_framework import viewsets, permissions
from rest_framework.decorators import api_view
from .models import User
from rest_framework.views import APIView
from rest_framework.response import Response
########


def indexActividad(request):
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
        form = modificarActividadForm(request.POST, request.FILES)
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
        form = modificarActividadForm(instance=activ)
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

def verPerfil(request, id):
    usuario = User.objects.get(id=id)
    context = {'perfil': perfil}
    return render(request, 'perfil.html', context)


def nuevoUsuario(request):
    if request.method == "POST":
        form = NuevoUsuarioForm(request.POST, request.FILES)
        if form.is_valid():

            form.save()
            login(request, user)

            return HttpResponseRedirect('/bienvenido')
    else:
        form = NuevoUsuarioForm()

    return render(request, 'nuevoUsuario.html', {'form': form})

def bienvenido():
    return render('bienvenido.html')

def loginSocio(request):
    form = LoginSocioForm()
    if request.method == "POST":
        # Añadimos los datos recibidos al formulario
        form = LoginSocioForm(data=request.POST)
        # Si el formulario es válido...
        if form.is_valid():
            # Recuperamos las credenciales validadas
            username = form.cleaned_data['username']

            # Verificamos las credenciales del usuario
            user = authenticate(username=username, password=username)

            # Si existe un usuario con ese nombre y contraseña
            if user is not None:
                # Hacemos el login manualmente
                login(request, user)
                # Y le redireccionamos a la portada
                return redirect('/')

    # Si llegamos al final renderizamos el formulario
    return render(request, "loginSocio.html", {'form': form})

def loginVoluntario(request):
    form = LoginVoluntarioForm()
    if request.method == "POST":
        # Añadimos los datos recibidos al formulario
        form = LoginVoluntarioForm(data=request.POST)
        # Si el formulario es válido...
        if form.is_valid():
            # Recuperamos las credenciales validadas
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            # Verificamos las credenciales del usuario
            user = authenticate(username=username, password=password)

            # Si existe un usuario con ese nombre y contraseña
            if user is not None:
                # Hacemos el login manualmente
                do_login(request, user)
                # Y le redireccionamos a la portada
                return redirect('/')

    # Si llegamos al final renderizamos el formulario
    return render(request, "loginVoluntario.html", {'form': form})

def logout(request):
    # Finalizamos la sesión
    do_logout(request)
    # Redireccionamos a la portada
    return redirect('/')



###------Cosas de REST FRAMEWORK API ----- #####
class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

class ActividadView(APIView):
    def get(self, request):
        actividades = Actividad.objects.all()
        # the many param informs the serializer that it will be serializing more than a single article.
        serializer = ActividadSerializer(actividades, many=True)
        return Response({"actividades": serializer.data, "prueba": None})

    def get(self, request, pk):
        actividades = Actividad.objects.all()
        # the many param informs the serializer that it will be serializing more than a single article.
        serializer = ActividadSerializer(actividades, many=True)
        return Response({"pruebaconPK": None})
