from django import forms

class AutosFormulario(forms.Form):
    marca = forms.CharField(max_length=40)
    modelo = forms.CharField(max_length=40)
    conductor = forms.CharField(max_length=40)
    foto = forms.ImageField(required=True)