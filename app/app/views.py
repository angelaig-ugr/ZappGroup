from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.http import HttpResponseRedirect
import datetime

from app.forms import *
# Create your views here.

#imports de serialziers
from .serializers import *
from rest_framework import viewsets, permissions, status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.parsers import FileUploadParser, MultiPartParser, FormParser
from .models import User, Actividad
from app.models.actividades import Adjuntado
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
# Con APIView mapeamos funciones a métodos de HTTP (GET, POST, ...)

# class UserViewSet(viewsets.ModelViewSet):
#     """
#     API endpoint that allows users to be viewed or edited.
#     """
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
#     permission_classes = [permissions.IsAuthenticated]

class GrupoView(APIView):
    def get(self, request):
        #grupos = get_list_or_404(Grupo.objects.all()).
        #serializer = GrupoSerializer(grupos, many=True)
        q = Grupo.objects.values('nombre').distinct()
        nombres = []
        for elem in q:
            nombres.append(elem["nombre"])

        return Response({"grupos": nombres})
        #return Response({"grupos": serializer.data})

    @api_view(['GET'])
    def getGrupo(request, nombre):
         usuarios = get_list_or_404(Grupo.objects.all(), nombre=nombre)
         serializer = GrupoSerializer(usuarios, many=True)

         data = []
         for usuario in usuarios:
             data.append(usuario.idUsuario.id)

         return Response({"nombre": nombre, "usuarios": data})

    def post(self, request):
        # Create an user from the above data
        serializer = GrupoSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            grupo_saved = serializer.save()
        return Response({"success": "Usuario añadido al grupo correctamente"})

        usuario = request.data.get('user')
        # Create an user from the above data
        serializer = SocioSerializer(data=usuario)
        if serializer.is_valid(raise_exception=True):
            user_saved = serializer.save()
        return Response({"success": "User '{}' created successfully".format(user_saved.username), "id" : user_saved.pk})

    def delete(self, request, nombre, pk):
        instance = get_object_or_404(Grupo.objects.all(), nombre=nombre, idUsuario=pk)
        instance = Grupo.objects.filter(nombre=nombre, idUsuario = pk)
        instance.delete()
        return Response({"message": "Usuario borrado del grupo"},status=204)





class SocioView(APIView):

    @api_view(['POST'])
    def loginSocio(request):
        idIntroducido = request.data.get('idUser')
        if(User.objects.filter(pk= idIntroducido, is_staff=False).count() == 1):
            return Response({"success": "User login successful" })
        else:
            return Response({"error": "No user found or user is staff" })

    def get(self, request, pk):
        if(pk == 0):
            usuario = get_list_or_404(User.objects.all(), is_staff=False)
            serializer = SocioSerializer(usuario, many=True)
        else:
            usuario = get_object_or_404(User.objects.all(), pk=pk, is_staff=False)
            serializer = SocioSerializer(usuario, many=False)

        return Response({"User": serializer.data})

    def post(self, request):
        usuario = request.data.get('user')
        # Create an user from the above data
        serializer = SocioSerializer(data=usuario)
        if serializer.is_valid(raise_exception=True):
            user_saved = serializer.save()
        return Response({"success": "User '{}' created successfully".format(user_saved.username), "id" : user_saved.pk})

    def put(self, request, pk):
        saved_user = get_object_or_404(User.objects.all(), pk=pk, is_staff=False)
        data = request.data.get('user')
        serializer = SocioSerializer(instance=saved_user, data=data, partial=True)
        if serializer.is_valid(raise_exception=True):
            user_saved = serializer.save()
        return Response({"success": "User '{}' updated successfully".format(user_saved.username), "id" : user_saved.pk})

    def delete(self, request, pk):
        # Get object with this pk
        user = get_object_or_404(User.objects.all(), pk=pk, is_staff=False)
        user.delete()
        return Response({"message": "User with id `{}` has been deleted.".format(pk)},status=204)

class FacilitadorView(APIView):

    @api_view(['POST'])
    def loginFacilitador(request):
        usernameIntroducido = request.data.get('username')
        passwordIntroducido = request.data.get('password')

        possibleUser = User.objects.filter(username= usernameIntroducido)
        if(possibleUser.count() == 1):
            if(possibleUser.get().is_staff and possibleUser.get().check_password(passwordIntroducido)):
                return Response({"success": "User login successful" })

        return Response({"error": "No user found or user is not staff" })

    def get(self, request, pk):
        if(pk == 0):
            usuario = get_list_or_404(User.objects.all(), is_staff=True)
            serializer = FacilitadorSerializer(usuario, many=True)
        else:
            usuario = get_object_or_404(User.objects.all(), pk=pk, is_staff=True)
            serializer = FacilitadorSerializer(usuario, many=False)

        return Response({"User": serializer.data})

    @api_view(['GET'])
    def allUsers(request):
        usuario = User.objects.all()
        serializer = FacilitadorSerializer(usuario, many=True)

        return Response({"User": serializer.data})

    def post(self, request):
        usuario = request.data.get('user')
        # Create an user from the above data
        serializer = FacilitadorSerializer(data=usuario)
        if serializer.is_valid(raise_exception=True):
            user_saved = serializer.save()
            user_saved.set_password(usuario.get("password"))
            user_saved.is_staff = True
            user_saved.save()

        return Response({"success": "User '{}' created successfully".format(user_saved.username), "id" : user_saved.pk})

    def put(self, request, pk):
        saved_user = get_object_or_404(User.objects.all(), pk=pk, is_staff=True)
        data = request.data.get('user')
        serializer = FacilitadorSerializer(instance=saved_user, data=data, partial=True)
        if serializer.is_valid(raise_exception=True):
            user_saved = serializer.save()
        return Response({"success": "User '{}' updated successfully".format(user_saved.username), "id" : user_saved.pk})

    def delete(self, request, pk):
        # Get object with this pk
        user = get_object_or_404(User.objects.all(), pk=pk, is_staff=True)
        user.delete()
        return Response({"message": "User with id `{}` has been deleted.".format(pk)},status=204)

class ActividadUsuarioView(APIView):
    # Devolver actividad de un usuario
    def get(self, request, pkUsuario, pkActividad):
        if(pkActividad == 0):
            actividades = get_list_or_404(Actividad.objects.all(), idUsuario= pkUsuario)
            serializer = ActividadSerializer(actividades, many=True)
        else:
            actividades = get_object_or_404(Actividad.objects.all(), idUsuario= pkUsuario, pk= pkActividad)
            serializer = ActividadSerializer(actividades, many=False)

        return Response({"Actividad": serializer.data})

    @api_view(['GET'])
    def actividadesNoEntregadas(request, pkUsuario):
        actividades = get_list_or_404(Actividad.objects.all(), idUsuario= pkUsuario, estado=Actividad.NO_ENTREGADO)
        serializer = ActividadSerializer(actividades, many=True)
        return Response({"Actividad": serializer.data})

    @api_view(['GET'])
    def actividadesEntregadas(request, pkUsuario):
        actividades = get_list_or_404(Actividad.objects.all(), idUsuario= pkUsuario, estado=Actividad.ENTREGADO)
        serializer = ActividadSerializer(actividades, many=True)
        return Response({"Actividad": serializer.data})

    @api_view(['GET'])
    def actividadesRevisadas(request, pkUsuario):
        actividades = get_list_or_404(Actividad.objects.all(), idUsuario= pkUsuario, estado=Actividad.REVISADO)
        serializer = ActividadSerializer(actividades, many=True)
        return Response({"Actividad": serializer.data})

    @api_view(['GET'])
    def actividadesNoRevisadas(request, pkProfesional):
        actividades = get_list_or_404(Actividad.objects.all(), idProfesional= pkProfesional, estado=Actividad.ENTREGADO)
        serializer = ActividadSerializer(actividades, many=True)
        return Response({"Actividad": serializer.data})


class ActividadView(APIView):

    def get(self, request, pk):
        if(pk == 0):
            actividades = Actividad.objects.all()
            serializer = ActividadSerializer(actividades, many=True)
        else:
            actividades = get_object_or_404(Actividad.objects.all(), pk= pk)
            serializer = ActividadSerializer(actividades, many=False)

        return Response({"Actividad": serializer.data})

    def post(self, request):
        actividad = request.data.get('actividad')
        # Create an article from the above data
        serializer = ActividadSerializer(data=actividad)
        if serializer.is_valid(raise_exception=True):
            actividad_saved = serializer.save()
        return Response({"success": "Actividad with id '{}' created successfully".format(actividad_saved.pk), "id" : actividad_saved.pk})

    def put(self, request, pk):
        saved_actividad = get_object_or_404(Actividad.objects.all(), pk=pk)
        data = request.data.get('actividad')
        serializer = ActividadSerializer(instance=saved_actividad, data=data, partial=True)
        if serializer.is_valid(raise_exception=True):
            actividad_saved = serializer.save()
        return Response({"success": "Actividad with id'{}' updated successfully".format(pk), "id" : actividad_saved.pk})

    def delete(self, request, pk):
        # Get object with this pk
        actividad = get_object_or_404(Actividad.objects.all(), pk=pk)
        actividad.delete()
        return Response({"message": "Actividad with id `{}` has been deleted.".format(pk)},status=204)

    @api_view(['PUT'])
    def cambiarEstado(request,pk,estado):
        actividad = get_object_or_404(Actividad.objects.all(), pk=pk)
        if(estado == 0): actividad.estado=Actividad.ENTREGADO
        elif(estado == 1): actividad.estado=Actividad.NO_ENTREGADO
        elif(estado == 2): actividad.estado=Actividad.REVISADO
        actividad.save()
        return Response({"success": "Actividad with id'{}' updated successfully".format(pk), "id" : actividad.pk})



class AdjuntadoView(APIView):
    def get(self, request, pk):
        adjuntados = get_list_or_404(Adjuntado.objects.all().order_by('fechaCreacion'), idActividad=pk)
        serializer = AdjuntadoSerializer(adjuntados, many=True)
        if serializer.is_valid(raise_exception=True):
            actividad_saved = serializer.save()
        return Response({"success": "Actividad with id'{}' updated successfully".format(pk), "id" : actividad_saved.pk})

    # def post(self, request):
    #     adjuntado = request.data.get('adjuntado')
    #     # Create an article from the above data
    #     serializer = AdjuntadoSerializer(data=adjuntado)
    #     if serializer.is_valid(raise_exception=True):
    #         adjuntado_saved = serializer.save()
    #     return Response({"success": "Adjuntado with id '{}' created successfully".format(adjuntado_saved.pk), "id" : adjuntado_saved.pk})

    def delete(self, request, pk):
        # Get object with this pk
        adjuntado = get_object_or_404(Adjuntado.objects.all(), pk=pk)
        adjuntado.delete()
        return Response({"message": "Adjuntado with id `{}` has been deleted.".format(pk)},status=204)

# Esto es lo de adjuntar (va aparte por lo de las parser_classes que no sé si joderá a otros métodos o no)
class FileUploadView(APIView):
    parser_classes = (FormParser, MultiPartParser)

    def put(self, request):
        adjuntado = AdjuntadoSerializer(data=request.data)
        if adjuntado.is_valid():
            adjuntado.save()
            return Response(adjuntado.data, status=status.HTTP_201_CREATED)
        else:
            return Response(adjuntado.errors, status=status.HTTP_400_BAD_REQUEST)

# Esto es lo de adjuntar (va aparte por lo de las parser_classes que no sé si joderá a otros métodos o no)
class CrearActividadView(APIView):
    parser_classes = (FormParser, MultiPartParser)

    def put(self, request):
        actividad = ActividadSerializer(data=request.data)
        if actividad.is_valid():
            actividad.save()
            return Response(actividad.data, status=status.HTTP_201_CREATED)
        else:
            return Response(actividad.errors, status=status.HTTP_400_BAD_REQUEST)
