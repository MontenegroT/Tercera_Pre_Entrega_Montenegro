from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def inicio(request):
    return HttpResponse(" Este es el inicio ")

def curso(request):
    return HttpResponse(" vista de las curso ")

def profesores(request):
    return HttpResponse(" vista de las profesores")

def Alumnos(request):
    return HttpResponse(" vista de las Alumnos ")

def actividades(request):
    return HttpResponse(" vista de las actividades ")
