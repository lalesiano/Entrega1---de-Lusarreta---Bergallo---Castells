from datetime import datetime
from django.shortcuts import render, redirect
import random
from MVT_App.models import Persona
from MVT_App.forms import BusquedaPersonaFormulario, PersonaFormulario


def crear_persona(request):
    
    if request.method == "POST": 
        formulario = PersonaFormulario(request.POST)
        
        if formulario.is_valid():
            data = formulario.cleaned_data           
            nombre = data["nombre"]
            apellido = data["apellido"]
            #-----------------
            fecha_ingreso = data.get("fecha_ingreso", datetime.now())
            #-----------------
            persona = Persona(nombre = nombre, apellido = apellido, numero_id = random.randrange(0,101), fecha_ingreso = fecha_ingreso)
            persona.save()
            
            return redirect("ver_persona")
    
    formulario = PersonaFormulario()
        
    return render(request,"crear_persona.html",{"formulario" : formulario})


def ver_persona(request):
    
    nombre = request.GET.get("nombre", None)
    
    if nombre:
        personas = Persona.objects.filter(nombre__icontains=nombre)
    else:
        personas = Persona.objects.all()
        
    formulario = BusquedaPersonaFormulario()
    
    return render(request, "ver_persona.html",{"personas" : personas, "formulario": formulario})


def index(request):
    
    return render(request, "index.html")


def about(request):
    
    return render(request, "about.html")