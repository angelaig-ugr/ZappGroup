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
from django.urls import path, re_path
from . import views


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

]
