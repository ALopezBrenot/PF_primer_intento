from django.db import models

# Create your models here.

class Posteo(models.Model):
    usuario = models.CharField(max_length=40)
    nombre_post = models.CharField(max_length=60)
    fecha = models.DateField(auto_now=True)
    contenido = models.CharField(max_length=450)

