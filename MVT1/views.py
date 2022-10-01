from django.http import HttpResponse
from django.template import Context, Template

def agregar_personas(request):
    cargar_archivo = open(r"C:\Users\alexis.delusarreta\Desktop\MVT_TP1\templates\template1.html", "r")
    template = Template(cargar_archivo.read())
    cargar_archivo.close()
    contexto = Context()
    template_renderizado = template.render(contexto)
    return HttpResponse(template_renderizado)

def ver_personas(request):
    return HttpResponse("<h1>ACA VES PERSONAS</h1>")