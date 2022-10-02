from datetime import date, datetime
from django.http import HttpResponse
from django.template import Context, Template, loader
import random
from MVT_App.models import Persona

def crear_persona(request,nombre,apellido):

    persona = Persona(nombre = nombre, apellido = apellido, numero_id = random.randrange(0,101), fecha_ingreso = datetime.now())
    persona.save()

    template = loader.get_template("crear_persona.html")
    template_renderizado = template.render({"personas" : persona})

    return HttpResponse(template_renderizado)

def ver_persona(request):

    personas = Persona.objects.all()


    template = loader.get_template("ver_persona.html")
    template_renderizado = template.render({"personas" : personas})

    return HttpResponse(template_renderizado)