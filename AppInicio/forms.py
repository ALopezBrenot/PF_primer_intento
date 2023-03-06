# Archivo que contiene los formularios de la App

from django import forms

class DocenteFormulario(forms.Form):
    nombre= forms.CharField()
    apellido= forms.CharField()
    materia= forms.CharField()
    mail= forms.EmailField()
    DNI= forms.IntegerField()

class AlumnoFormulario(forms.Form):
    nombre= forms.CharField()
    apellido= forms.CharField()
    curso= forms.IntegerField()
    mail= forms.EmailField()
    DNI= forms.IntegerField()
    fecha_nacimiento= forms.DateField()

class PracticaFormulario(forms.Form):
    nombre= forms.CharField()
    materia= forms.CharField()
    curso= forms.IntegerField()
    fecha= forms.DateField()