from django import forms
from django.forms import ModelForm
from django.core.exceptions import NON_FIELD_ERRORS

from app.models import *


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
        fields = ['idUsuario', 'idProfesional', 'descripcion', 'video', 'pdf', 'comentario']

    def clean(self):
        cd = self.cleaned_data
'''
class ProfesionalForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = User
    
    def clean(self):
        cleaned_data = self.cleaned_data
'''

class NuevoUsuarioForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password', 'is_staff', 'fechaNacimiento', 'foto', 'coordinador']

    def clean(self):
        cleaned_data = self.cleaned_data

class LoginSocioForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username']

    def clean(self):
        cleaned_data = self.cleaned_data

class LoginVoluntarioForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password']
    
    def clean(self):
        cleaned_data = self.cleaned_data