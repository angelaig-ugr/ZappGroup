# Generated by Django 3.1.2 on 2020-11-10 09:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20201110_0911'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='coordinador',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='user',
            name='fechaNacimiento',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='foto',
            field=models.ImageField(blank=True, null=True, upload_to=None),
        ),
    ]
