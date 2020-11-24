from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from app.models.gestionUsuario import User
from app.models.actividades import Actividad, Categoria

admin.site.register(User, UserAdmin)
admin.site.register(Categoria)
admin.site.register(Actividad)
