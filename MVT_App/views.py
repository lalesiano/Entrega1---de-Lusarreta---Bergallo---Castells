from datetime import date, datetime
from django.http import HttpResponse
from django.template import Context, Template, loader
from django.shortcuts import render
import random
from MVT_App.models import Persona

def crear_persona(request):
    nombre = request.POST.get("nombre")
    apellido = request.POST.get("apellido")
    persona = Persona(nombre = nombre, apellido = apellido, numero_id = random.randrange(0,101), fecha_ingreso = datetime.now())
    persona.save()
    return render(request,"crear_persona.html",{})

def ver_persona(request):
    personas = Persona.objects.all()
    return render(request, "ver_persona.html",{"personas" : personas})

def index(request):
    return render(request, "index.html")