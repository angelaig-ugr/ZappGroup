from .models import User, Actividad
from rest_framework import serializers

class UserSerializer(serializers.HyperlinkedModelSerializer):
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


class ActividadSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Actividad
        fields = ['idUsuario', 'idProfesional']

        def create(self, validated_data):
            return Actividad.objects.create(**validated_data)
        
        # def update(self, user, validated_data):