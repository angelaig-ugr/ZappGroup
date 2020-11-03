# Generated by Django 3.1.2 on 2020-10-26 21:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=100)),
                ('edad', models.IntegerField()),
                ('categoria', models.CharField(choices=[('Alumno', 'Alumno'), ('Profesional', 'Profesional')], default='Alumno', max_length=200)),
            ],
        ),
    ]