from django.db import models

# Create your models here.

class Practica(models.Model):
    nombre = models.CharField(max_length=50)
    materia = models.CharField(max_length=30)
    curso = models.IntegerField()
    fecha = models.DateField()

    def __str__(self):
        return (self.nombre + '/' + self.materia)


class Docente(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    materia = models.CharField(max_length=30)
    mail = models.EmailField()
    DNI = models.IntegerField()

    def __str__(self):
        return (self.nombre + ' ' + self.apellido)


class Alumno(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    curso = models.IntegerField()
    mail = models.EmailField()
    DNI = models.IntegerField()
    fecha_nacimiento = models.DateField()

    def __str__(self):
        return (self.nombre + ' ' + self.apellido)
