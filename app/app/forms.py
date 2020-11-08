from django import forms
from django.forms import ModelForm
from django.core.exceptions import NON_FIELD_ERRORS

from models import *


class nuevaActividadForm(ModelForm):
    class Meta:
        model = Actividad
        #Falta imagen
        fields = ['idUsuario', 'idProfesional', 'descripcion', 'video', 'pdf', 'comentario']

    def clean(self):
        cleaned_data = self.cleaned_data

class modificarActividadForm(ModelForm):
    class Meta:
        model = Actividad
        #Falta imagen
        fields = fields = ['idUsuario', 'idProfesional', 'descripcion', 'video', 'pdf', 'comentario']

    def clean(self):
        cd = self.cleaned_data

class ProfesionalForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = Profesional
    
    def clean(self):
        cleaned_data = self.cleaned_data


class NuevoUsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['nombre', 'email', 'fechaNacimiento', 'foto', 'coordinador']

    def clean(self):
        cleaned_data = self.cleaned_data


class LoginUsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['id']

    def clean(self):
        cleaned_data = self.cleaned_data

class LoginProfesionalForm(forms.ModelForm):
    class Meta:
        model = Profesional
        fields = ['id', 'password']
    
    def clean(self):
        cleaned_data = self.cleaned_data