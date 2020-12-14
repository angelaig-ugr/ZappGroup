from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from app.models.gestionUsuario import User, Grupo
from app.models.actividades import Actividad, Categoria, Adjuntado

admin.site.register(User, UserAdmin)
admin.site.register(Categoria)
admin.site.register(Actividad)
admin.site.register(Adjuntado)
admin.site.register(Grupo)
