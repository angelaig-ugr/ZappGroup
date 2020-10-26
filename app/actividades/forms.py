from django import forms
from django.forms import ModelForm
from django.core.exceptions import NON_FIELD_ERRORS

from actividades.models import *

class nuevaActividadForm(ModelForm):
    class Meta:
        model = Actividad
        #Falta imagen
        fields = ['idUsuario', 'idProfesional', 'descripcion', 'video', 'pdf', 'comentario']

    def clean(self):
        cleaned_data = self.cleaned_data

class modificarActividad(ModelForm):
    class Meta:
        model = Actividad
        #Falta imagen
        fields = fields = ['idUsuario', 'idProfesional', 'descripcion', 'video', 'pdf', 'comentario']

    def clean(self):
        cd = self.cleaned_data