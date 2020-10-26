from django.db import models
from gestionUsuario.models import Usuario

# Create your models here.

class Actividad(models.Model):
	idUsuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
	idProfesional = models.ForeignKey(Usuario, on_delete=models.CASCADE)
	descripcion = models.CharField(maxlength=5000)
	video = models.URLField()
	imagen = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=100, **options)
	pdf = models.FileField(upload_to=None, max_length=100)
	comentario = models.CharField(maxlength=5000)
	fechaEntrega = models.DateField(auto_now=False, auto_now_add=False)
	fechaCreacion = models.DateField(auto_now=False, auto_now_add=False)
	ENTREGADO = 'Entregado'
	NO_ENTREGADO = 'No entregado'
	REVISADO = 'Revisado'

	OPCIONES = [
		(ENTREGADO, 'Entregado'),
		(NO_ENTREGADO, 'No entregado'),
		(REVISADO, 'Revisado'),
	]
