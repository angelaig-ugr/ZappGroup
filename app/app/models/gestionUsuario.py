from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class User(AbstractUser):
	#Abstract user ya tiene los campos: username, first_name, last_name, email,
	#  password (que sea el mismo que el username para los socios), last_login etc
	fechaNacimiento = models.DateField(auto_now=False, auto_now_add=False)
	es_socio = models.BooleanField(default=False)
	foto = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=100, blank=True)
	coordinador = models.ForeignKey(Usuario, on_delete=models.CASCADE, blank=True) #solo los socios, se pone a si mismo

'''

class Profesional(AbstractUser):
	#nombre = models.CharField(max_length=100) --username
	#first_name
	#last_name
	#
	#email = models.EmailField(max_length=100)
	#password = models.CharField(max_length=50)
	fechaNacimiento = models.DateField(auto_now=False, auto_now_add=False)


class Usuario(AbstractUser):
	#nombre = models.CharField(max_length=100)
	#email = models.EmailField(max_length=100)
	#password 
	#fechaNacimiento = models.DateField(auto_now=False, auto_now_add=False)
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
'''