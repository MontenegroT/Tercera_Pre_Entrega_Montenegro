from django.db import models
# Create your models here.


class Curso(models.Model):
    nombre=models.CharField(max_length=30)
    turno=models.CharField(max_length=30)
    duracion=models.IntegerField()

class Profesores(models.Model):
    nombre=models.CharField(max_length=30)
    correo=models.EmailField()
    profesion=models.CharField(max_length=30)
    cursos_asignados=models.IntegerField()

class Alumnos(models.Model):
     nombre=models.CharField(max_length=30)
     documento=models.IntegerField()
     correo=models.EmailField()
     cursos_inscripto=models.IntegerField()

class Actividades(models.Model):
    tipo=models.CharField(max_length=30)
    fecha_inicio=models.IntegerField()
    fecha_entrega=models.IntegerField()
    entrega=models.BooleanField()
    


