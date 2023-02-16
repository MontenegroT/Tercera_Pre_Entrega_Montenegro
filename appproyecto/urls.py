from django.urls import path
from appproyecto import views

urlpatterns = [
    path('', views.inicio, name="Inicio"),
    path('Cursos/', views.curso, name="Cursos"),
    path('Profesores/', views.profesores, name="Profesores"),
    path('Alumnos/', views.alumnos, name="Alumnos"),
    path('Actividades/', views.actividades, name="Actividades"),
    path('cursoFormulario/', views.cursoFormulario, name="cursoFormulario"),
    path('profesoresform/', views.profesoresform, name="profesoresform"),
    path('alumnosform/', views.alumnosform, name="alumnosform"),
    path('actividadesform/', views.actividadform, name="actividadesform"),
    path('buscarInfo/', views.buscarInfo, name="buscarInfo"),
    path('buscar/', views.buscar)
]