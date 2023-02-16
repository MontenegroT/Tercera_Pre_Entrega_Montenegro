from django import forms

class CursoFormulario(forms.Form):
    curso=forms.CharField(max_length=30)
    turno=forms.CharField(max_length=30)