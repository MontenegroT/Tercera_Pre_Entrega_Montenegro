from django.urls import path
from appproyecto import views


urlpatterns = [
    path('', views.inicio),
    path('Curso/', views.curso),
    path('Profesores/', views.profesores),
    path('Alumnos/', views.actividades),
    path('Actividades/', views.actividades),
]