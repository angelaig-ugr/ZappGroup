from django.db import models

# Create your models here.

class Usuario(models.Model):
	nombre = models.CharField(max_length=100)
	email = models.EmailField(max_length=100)
	# usuarioAsociado = models.ListCharField(CharField)
	edad = models.IntegerField()
	# foto = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=100, blank=True)
	ALUMNO = 'Alumno'
	PROFESIONAL = 'Profesional'
	OPCIONES = [
		(ALUMNO, 'Alumno'),
		(PROFESIONAL, 'Profesional'),
	]
	categoria = models.CharField(choices=OPCIONES, max_length=200, default=ALUMNO)


#def __str__(self):
#    return str(self.id) + '-' + self.nombre + '-' + '-' + self.caracter + '-' self.email
