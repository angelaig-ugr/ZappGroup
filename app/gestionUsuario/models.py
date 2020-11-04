from django.db import models

# Create your models here.

class Profesional(models.Model):
	nombre = models.CharField(max_length=100)
	email = models.EmailField(max_length=100)
	password = models.CharField(max_length=50)
	fechaNacimiento = models.DateField(auto_now=False, auto_now_add=False)


class Usuario(models.Model):
	nombre = models.CharField(max_length=100)
	email = models.EmailField(max_length=100)
	fechaNacimiento = models.DateField(auto_now=False, auto_now_add=False)
	foto = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=100, blank=True)
	coordinador = models.ForeignKey(Profesional, on_delete=models.CASCADE, blank=True)
	
	"""ALUMNO = 'Alumno'
	PROFESIONAL = 'Profesional'
	OPCIONES = [
		(ALUMNO, 'Alumno'),
		(PROFESIONAL, 'Profesional'),
	]
	categoria = models.CharField(choices=OPCIONES, max_length=200, default=ALUMNO)"""



#def __str__(self):
#    return str(self.id) + '-' + self.nombre + '-' + '-' + self.caracter + '-' self.email
