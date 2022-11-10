from django import forms
from ckeditor.fields import RichTextFormField

class AutosFormulario(forms.Form):
    marca = forms.CharField(max_length=40)
    modelo = forms.CharField(max_length=40)
    conductor = forms.CharField(max_length=40)
    foto = forms.ImageField(required=True)

class Autos(forms.Forms):
    modelo = forms.CharField(max_length=20)
    marca = forms.CharField(max_length=20)
    conductor = forms.CharField(max_length=50)
    foto = forms.ImageField(upload_to="foto")
    descripcion = RichTextFormField (required=False)

