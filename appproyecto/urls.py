from django.urls import path
from appproyecto import views

urlpatterns = [
    path('', views.inicio, name="Inicio"),
    path('Cursos/', views.curso, name="Cursos"),
    path('Profesores/', views.profesores, name="Profesores"),
    path('Alumnos/', views.alumnos, name="Alumnos"),
    path('Actividades/', views.actividades, name="Actividades"),
    path('cursoFormulario/', views.CursoFormulario, name="cursoFormulario"),
]