from django import forms
from django import forms
from django.forms import CharField

class PersonaFormulario(forms.Form):
    nombre = forms.CharField(max_length=30, required=True)
    apellido = forms.CharField(max_length=30, required=True)
    numero_id = forms.IntegerField(required=False)
    fecha_ingreso = forms.DateField(required=False)
    
class BusquedaPersonaFormulario(forms.Form):
    nombre = forms.CharField(max_length=30, required=False)
