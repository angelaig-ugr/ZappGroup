from .models import *
from app.models.actividades import Adjuntado
from rest_framework import serializers

class FacilitadorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password', 'email', 'fechaNacimiento']

        def create(self, validated_data):
            return User.objects.create(**validated_data)

        def update(self, user, validated_data):
            user.username = validated_data.get('username', user.username)
            user.password = validated_data.get('password', user.password)
            user.email = validated_data.get('email', user.email)
            user.fechaNacimiento = validated_data.get('fechaNacimiento', user.fechaNacimiento)

            user.save()
            return user

class SocioSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'fechaNacimiento']

        def create(self, validated_data):
            return User.objects.create(**validated_data)

        def update(self, user, validated_data):
            user.username = validated_data.get('username', user.username)
            user.email = validated_data.get('email', user.email)
            user.fechaNacimiento = validated_data.get('fechaNacimiento', user.fechaNacimiento)

            user.save()
            return user


class ActividadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actividad
        fields = ['idUsuario', 'idProfesional', 'categoria', 'nombre', 'descripcion']

        # def create(self, validated_data):
        #     return Actividad.objects.create(**validated_data)
        #
        # def update(self, activity, validated_data):
        #     activity.idUsuario = validated_data.get('idUsuario', activity.idUsuario)
        #     activity.idProfesional = validated_data.get('idProfesional', activity.idProfesional)
        #
        #     activity.save()
        #     return activity

class AdjuntadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Adjuntado
        fields = ['idActividad', 'is_staff', 'pdf', 'comentario', 'video']