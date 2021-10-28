from django import forms
from django.forms import ModelForm
from .models import Competidor

class inscripcionForm(ModelForm):
    class Meta:
        model = Competidor
        fields = ['nombre', 'apellido', 'categoria', 'graduacion', 'academia', 'instructor', 'celular', 'dni']

        