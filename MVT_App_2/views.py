from django.shortcuts import render, redirect
from MVT_App_2.forms import AutosFormulario
from MVT_App_2.models import Autos

def ver_autos(request):

     autos = Autos.objects.all()

     return render(request,"mvt2/ver_autos.html",{"autos": autos})


def crear_auto(request):

     formulario = AutosFormulario()

     

     return render (request, 'mvt2/crear_auto.html', {'formulario': formulario})