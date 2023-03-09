from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic.edit import UpdateView
from AppInicio.forms import *
from AppInicio.models import *

# Create your views here.

def Inicio (request):
    return render(request, 'AppInicio/inicio.html')


def Docentes(request):

    profesores = Docente.objects.all()

    if request.method == 'POST':
        mi_formulario = DocenteFormulario(request.POST)

        #Se validan los datos recibidos
        if mi_formulario.is_valid():
            info = mi_formulario.cleaned_data
            docente = Docente(nombre=info['nombre'],
                              apellido=info['apellido'],
                              materia=info['materia'],
                              mail=info['mail'],
                              DNI=info['DNI'])
            docente.save()
            return redirect('inicio')
    else:
        mi_formulario = DocenteFormulario()

    return render(request, 'AppInicio/docentes.html', {'formulario_docente': mi_formulario, 'profesores': profesores})

def Alumnos(request):

    alumnos = Alumno.objects.all()

    if request.method == 'POST':
        mi_formulario = AlumnoFormulario(request.POST)

        if mi_formulario.is_valid():
            info = mi_formulario.cleaned_data
            alumno = Alumno(nombre=info['nombre'],
                            apellido=info['apellido'],
                            curso=info['curso'],
                            mail=info['mail'],
                            DNI=info['DNI'],
                            fecha_nacimiento=info['fecha_nacimiento'])
            alumno.save()
            return redirect('inicio')
    else:
        mi_formulario = AlumnoFormulario()

    return render(request, 'AppInicio/alumnos.html', {'formulario_alumno': mi_formulario, 'alumnos': alumnos})


def Practicas(request):

    practicas = Practica.objects.all()

    if request.method == 'POST':
        mi_formulario = PracticaFormulario(request.POST)

        if mi_formulario.is_valid():
            info = mi_formulario.cleaned_data
            practica = Practica(nombre=info['nombre'],
                                materia=info['materia'],
                                curso=info['curso'],
                                fecha=info['fecha'])
            practica.save()
            return redirect('inicio')

    else:
        mi_formulario = PracticaFormulario()

    return render(request, 'AppInicio/practicas.html', {'formulario_practica': mi_formulario, 'practicas': practicas})

# Vistas para búsqueda de clases por fecha:

def busqueda_clase(request):
    return render(request, 'AppInicio/inicio.html')

def buscar(request):
    if request.GET['fecha']:
        mi_fecha = request.GET['fecha']
        resultado = Practica.objects.filter(fecha__icontains = mi_fecha)

        return render(request, 'AppInicio/inicio.html', {'clase':resultado , 'fecha': mi_fecha})
    
    else:
        respuesta = 'Debes ingresar una fecha para poder buscar.'

    return HttpResponse (respuesta)

# Vistas para CRUD
# Delete
def eliminar_docente(request, docente_id):
    profesor = Docente.objects.get(id = docente_id)
    profesor.delete()
    
    profesores = Docente.objects.all()
    mi_formulario = DocenteFormulario()
    
    return render(request,'AppInicio/docentes.html', {'profesores':profesores, 'formulario_docente': mi_formulario})

def eliminar_practica(request, practica_id):
    practica = Practica.objects.get(id = practica_id)
    practica.delete()

    practicas = Practica.objects.all()
    mi_formulario = PracticaFormulario()

    return render (request, 'AppInicio/practicas.html', {'practicas': practicas, 'formulario_practica': mi_formulario})

def eliminar_alumno(request, alumno_id):
    alumno = Alumno.objects.get(id = alumno_id)
    alumno.delete()

    alumnos = Alumno.objects.all()
    mi_formulario = AlumnoFormulario()

    return render(request, 'AppInicio/alumnos.html', {'alumnos': alumnos, 'formulario_alumno': mi_formulario})

# Vistas para Update 

