from dataclasses import fields
from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import UserCreationForm

class MiFormularioDeCreacion(UserCreationForm):   
    email = forms.CharField()
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Repetir Contraseña", widget=forms.PasswordInput)
    
    class Meta:
        model = User
        fields = ["username", "email", "password1","password2"]
        help_text = {key: " " for key in fields}
    
class EditarPerfilFormulario(forms.Form):
    email = forms.CharField()
    first_name = forms.CharField(label="Nombre")
    last_name = forms.CharField(label="Apellido")
    avatar = forms.ImageField(required=False)
    