from django.db import models
from gestionUsuario.models import Usuario
import datetime

# Create your models here.

class Actividad(models.Model):
	idUsuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, limit_choices_to={'categoria':'Alumno'})
	idProfesional = models.ForeignKey(Usuario, related_name='idProfesional', on_delete=models.CASCADE, limit_choices_to={'categoria':'Profesional'})
	descripcion = models.CharField(max_length=5000, blank=True)
	video = models.URLField(blank=True)

	# Hace falta Pillow según el compilador
	# imagen = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=100)
	
	pdf = models.FileField(upload_to=None, max_length=100, blank=True)
	comentario = models.CharField(max_length=5000, blank=True)
	fechaEntrega = models.DateField(auto_now=False, auto_now_add=False, blank=True, null=True, default=None)
	fechaCreacion = models.DateField(auto_now=False, auto_now_add=False)
	
	ENTREGADO = 'Entregado'
	NO_ENTREGADO = 'No entregado'
	REVISADO = 'Revisado'

	OPCIONES = [
		(ENTREGADO, 'Entregado'),
		(NO_ENTREGADO, 'No entregado'),
		(REVISADO, 'Revisado'),
	]

	estado = models.CharField(choices=OPCIONES, max_length=200, default=NO_ENTREGADO)
