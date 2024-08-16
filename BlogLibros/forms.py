from django import forms 
from .models import Libro, Autor, Lectores

class LibroFormulario(forms.Form):
    titulo = forms.CharField()
    autor = forms.CharField()
    genero = forms.CharField()
    
class BusquedaFormulario(forms.Form):
    buscolibro = forms.CharField()

class AutorFormulario(forms.Form):
    nombre = forms.CharField()
    apellido = forms.CharField()
        
class LectorFormulario(forms.Form):
    nombre = forms.CharField()
    apellido = forms.CharField()
    pais = forms.CharField()
    
