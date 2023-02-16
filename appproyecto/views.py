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
            profesor=Profesores( nombre=datos['nombre'], correo=datos['correo'], profesion=datos['profesion'], cursos_asignados=datos['cursos_asignados'])
            profesor.save()
            return render(request,'appproyecto/Inicio.html')
    else:
        miFormulario = ProfesoresForm()
    return render(request,'appproyecto/profesoresform.html', {"miFormulario":miFormulario})

def alumnosform(request):
    if request.method == 'POST':
        miFormulario = AlumnosForm(request.POST)
        print(miFormulario)
        if miFormulario.is_valid:
            informacion = miFormulario.cleaned_data
            alumnos=Alumnos( nombre=informacion['nombre'], correo=informacion['correo'], cursos_inscripto=informacion['cursos_inscripto'], documento=informacion['documento'])
            alumnos.save()
            return render(request,'appproyecto/Inicio.html')
    else:
        miFormulario = AlumnosForm()
    return render(request,'appproyecto/alumnosform.html', {"miFormulario":miFormulario})

def actividadform(request):
    if request.method == 'POST':
        miFormulario = ActividadForm(request.POST)
        print(miFormulario)
        if miFormulario.is_valid:
            informacion = miFormulario.cleaned_data
            actividad=Actividades( tipo=informacion['tipo'], fecha_inicio=informacion['fecha_inicio'], fecha_entrega=informacion['fecha_entrega'], entrega=informacion['entrega'])
            actividad.save()
            return render(request,'appproyecto/Inicio.html')
    else:
        miFormulario = ActividadForm()
    return render(request,'appproyecto/actividadesform.html', {"miFormulario":miFormulario})
