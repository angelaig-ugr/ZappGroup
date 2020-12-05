from django.db import models
from app.models.gestionUsuario import User
import datetime

# Create your models here.

class Categoria(models.Model):
	nombre=models.CharField(max_length=50)

	#Hace Falta Pillow
	#pictograma=models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=100)

class Actividad(models.Model):
	idUsuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name="socio")
	idProfesional = models.ForeignKey(User, on_delete=models.CASCADE, related_name="voluntario")

	categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE,default=None)
	descripcion = models.CharField(max_length=5000, blank=True)
	video = models.URLField(blank=True)

	# Hace falta Pillow según el compilador
	# imagen = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=100)

	pdf = models.FileField(upload_to=None, max_length=100, blank=True)
	comentario = models.CharField(max_length=5000, blank=True)
	fechaEntrega = models.DateField(auto_now=False, auto_now_add=False, blank=True, null=True, default=None)
	fechaCreacion = models.DateField(auto_now=False, auto_now_add=True)

	ENTREGADO = 'Entregado'
	NO_ENTREGADO = 'No entregado'
	REVISADO = 'Revisado'

	OPCIONES = [
		(ENTREGADO, 'Entregado'),
		(NO_ENTREGADO, 'No entregado'),
		(REVISADO, 'Revisado'),
	]

	estado = models.CharField(choices=OPCIONES, max_length=200, default=NO_ENTREGADO)

class Adjuntado(models.Model):
	idActividad = models.ForeignKey(Actividad, on_delete=models.CASCADE, related_name="idActividad")
	fechaCreacion = models.DateField(auto_now=False, auto_now_add=True)
	is_staff = models.BooleanField(blank=False)
	pdf = models.FileField(upload_to=None, max_length=100, blank=True)
	comentario = models.CharField(max_length=5000, blank=True)
	video = models.URLField(blank=True)
	imagen = models.ImageField(height_field=None, width_field=None, max_length=100)
