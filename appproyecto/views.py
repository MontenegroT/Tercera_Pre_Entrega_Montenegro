from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def inicio(request):
    return render(request,'appproyecto/inicio.html')
    #return HttpResponse(" Este es el inicio ")

def curso(request):
    #return HttpResponse(" vista de las curso ")
    return render(request,'appproyecto/curso.html')

def profesores(request):
    #return HttpResponse(" vista de las profesores")
    return render(request,'appproyecto/profesores.html')

def Alumnos(request):
    #return HttpResponse(" vista de las Alumnos ")
    return render(request,'appproyecto/alumnos.html')

def actividades(request):
    #return HttpResponse(" vista de las actividades ")
    return render(request,'appproyecto/avtividades.html')
