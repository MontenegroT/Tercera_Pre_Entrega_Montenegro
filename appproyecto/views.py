from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from .froms import *
# Create your views here.

def inicio(request):
    return render(request,'appproyecto/Inicio.html')
    #return HttpResponse(" Este es el inicio ")

def curso(request):
    #return HttpResponse(" vista de las curso ")
    return render(request,'appproyecto/curso.html')

def profesores(request):
    #return HttpResponse(" vista de las profesores")
    return render(request,'appproyecto/profesores.html')

def alumnos(request):

    #return HttpResponse(" vista de las Alumnos ")
    return render(request,'appproyecto/alumnos.html')

def actividades(request):
    #return HttpResponse(" vista de las actividades ")
    return render(request,'appproyecto/actividades.html')

"""
def cursoFormulario(request):
    #return HttpResponse(" vista de las actividades ")
    if request.method == 'POST':
        cursos=Curso(request.POST['Cursos'], request.POST['Comision'])
        cursos.save()
        #return render(request, "appproyecto/ /Inicio.html")
        return render(request,'appproyecto/Inicio.html')
    return render(request,'appproyecto/cursoFormulario.html')
 """
def cursoFormulario(request):
    if request.method =='POST':
        miFormulario = CursoFormulario(request.POST)
        print(miFormulario)
        if miFormulario.is_valid:
            informacion = miFormulario.cleaned_data
            cursos=Curso( nombre=informacion['Cursos'], comision=informacion['Comision'])
            cursos.save()
            return render(request,'appproyecto/Inicio.html')
    else:
        miFormulario = CursoFormulario()

    return render(request,'appproyecto/cursoFormulario.html', {"miFormulario":miFormulario})
