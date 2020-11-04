from django.urls import path, re_path

from . import views
#from gestion_recursos import views NO SE PUEDE HACER

# La ruta '' equivale a /tareas en el navegador, hay muchos ejemplos en el fichero urls de gestion_animales

urlpatterns = [
    path('', views.index, name='index'),
    re_path(r'^nuevaActividad$', views.nuevaActividad, name='nuevaActividad'),
    re_path(r'^verActividadesRealizadas/(?P<id>[0-9]+)$', views.verActividadesRealizadas, name='verActividadesRealizadas'),
    re_path(r'^eliminarActividad/(?P<id>[0-9]+)$', views.eliminarActividad, name='eliminarActividad'),
    re_path(r'^verActividad/(?P<id>[0-9]+)$', views.verActividad, name='verActividad'),
    re_path(r'^verActividadesUsuario/(?P<id>[0-9]+)$', views.verActividadesUsuario, name='verActividadesUsuario'),
]