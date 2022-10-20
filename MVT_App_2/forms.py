from django import forms
from django import forms

class AutosFormulario(forms.Form):
    modelo = forms.CharField(max_length=40)
    marca = forms.CharField(max_length=40)
    ano = forms.IntegerField()