from django.http import HttpResponse

def agregar_personas(request):
    return HttpResponse("<h1>ACA AGREGAS PERSONAS</h1>")

def ver_personas(request):
    return HttpResponse("<h1>ACA VES PERSONAS</h1>")