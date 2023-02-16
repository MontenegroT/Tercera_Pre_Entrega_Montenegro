from django.shortcuts import render
from django.http import HttpResponse
from appproyecto.models import *
from appproyecto.forms import *
# Create your views here.

def inicio(request):
    return render(request,'appproyecto/Inicio.html')

def curso(request):
    return render(request,'appproyecto/curso.html')

def profesores(request):
    return render(request,'appproyecto/profesores.html')

def alumnos(request):
  return render(request,'appproyecto/alumnos.html')

def actividades(request):
    return render(request,'appproyecto/actividades.html')

def cursoFormulario(request):
    if request.method == 'POST':
        miFormulario = CursoFormulario(request.POST)
        print(miFormulario)
        if miFormulario.is_valid:
            informacion = miFormulario.cleaned_data
            cursos=Curso( nombre=informacion['curso'], turno=informacion['turno'], duracion=informacion['duracion'], comision=informacion['comision'])
            cursos.save()
            return render(request,'appproyecto/Inicio.html')
    else:
        miFormulario = CursoFormulario()

    return render(request,'appproyecto/cursoFormulario.html', {"miFormulario":miFormulario})

def profesoresform(request):
    if request.method == 'POST':
        miFormulario = ProfesoresForm(request.POST)
        print(miFormulario)
        if miFormulario.is_valid:
            datos = miFormulario.cleaned_data
            profesor=Profesores( nombre=datos['nombnre'], correo=datos['correo'], profesion=datos['profesion'], comisioncursos_asignados=datos['cursos_asignados'])
            profesor.save()
            return render(request,'appproyecto/Inicio.html')
    else:
        miFormulario = ProfesoresForm()

    return render(request,'appproyecto/profesoresform.html', {"miFormulario":miFormulario})
