#Aquí se detallan todas las urls de la App Inicio

from django.urls import path
from AppInicio import views

urlpatterns = [
    path('inicio/', views.Inicio, name='inicio'),
    path('docentes/', views.Docentes, name='docentes'),
    path('alumnos/', views.Alumnos, name='alumnos'),
    path('practicas/', views.Practicas, name='practicas'),
    path('busqueda-clase/', views.busqueda_clase, name='busqueda-clase'),
    path('buscar/', views.buscar, name='buscar'),
]