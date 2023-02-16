from django import forms

class CursoFormulario(forms.Form):
    curso=forms.CharField()
    turno=forms.CharField()
    duracion=forms.IntegerField()
    comision=forms.IntegerField()

class ProfesoresForm(forms.Form):
    nombre=forms.CharField(max_length=30)
    correo=forms.EmailField()
    profesion=forms.CharField(max_length=30)
    cursos_asignados=forms.IntegerField()

class AlumnosForm(forms.Form):
     nombre=forms.CharField(max_length=30)
     documento=forms.IntegerField()
     correo=forms.EmailField()
     cursos_inscripto=forms.IntegerField()

class ActividadForm(forms.Form):
    tipo=forms.CharField(max_length=30)
    fecha_inicio=forms.IntegerField()
    fecha_entrega=forms.IntegerField()
    entrega=forms.BooleanField()
