from django import forms
from django.forms import ModelForm
from gestionUsuario.models  import Profesional

class ProfesionalForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = Profesional