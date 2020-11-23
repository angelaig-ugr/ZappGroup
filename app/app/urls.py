"""app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""


from django.contrib import admin
from django.urls import include, path, re_path
from . import views
from rest_framework import routers

from .views import *


#### Cosas del rest framework ###
# router = routers.DefaultRouter()
# router.register(r'getAllUsers', views.UserViewSet)
#router.register(r'hello', views.hello_world)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('perfil', views.verPerfil, name='perfil'),
    path('loginSocio', views.loginSocio, name='loginSocio'),
    path('loginVoluntario', views.loginVoluntario, name='loginVoluntario'),
    path('nuevoUsuario', views.nuevoUsuario, name='nuevoUsuario'),
    path('bienvenido', views.bienvenido, name='bienvenido'),
    path('', admin.site.urls, name='indexActivdad'),
    re_path(r'^nuevaActividad$', views.nuevaActividad, name='nuevaActividad'),
    re_path(r'^verActividadesRealizadas/(?P<id>[0-9]+)$', views.verActividadesRealizadas, name='verActividadesRealizadas'),
    re_path(r'^eliminarActividad/(?P<id>[0-9]+)$', views.eliminarActividad, name='eliminarActividad'),
    re_path(r'^verActividad/(?P<id>[0-9]+)$', views.verActividad, name='verActividad'),
    re_path(r'^verActividadesUsuario/(?P<id>[0-9]+)$', views.verActividadesUsuario, name='verActividadesUsuario'),
    # path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    
    path('actividad/<int:pk>', ActividadView.as_view()),
    path('actividad/<int:pkUsuario>/<int:pkActividad>', ActividadUsuarioView.as_view()),
    
    path('socio/<int:pk>', SocioView.as_view()),
    path('crearSocio/', SocioView.as_view()),
    path('loginSocio/', SocioView.loginSocio),

    path('facilitador/<int:pk>', FacilitadorView.as_view()),
    path('crearFacilitador/', FacilitadorView.as_view()),
    path('loginFacilitador/', FacilitadorView.loginFacilitador),
]
