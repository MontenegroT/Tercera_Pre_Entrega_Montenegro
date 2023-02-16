from django.urls import path
from appproyecto import views

urlpatterns = [
    path('', views.inicio),
    path('curso/', views.curso),
    path('profesores/', views.profesores),
    path('alumnos/', views.actividades),
    path('actividades/', views.actividades),
]