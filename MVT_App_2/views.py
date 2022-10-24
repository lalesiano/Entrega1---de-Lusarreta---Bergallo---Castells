
from django.shortcuts import render, redirect
import MVT_App_2
from MVT_App_2.models import Autos
from MVT_App_2.forms import AutosFormulario
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

def ver_autos(request):

     autos = Autos.objects.all()

     return render(request,"mvt2/ver_autos.html",{"autos": autos})


def crear_auto(request): 

     if request.method == 'POST':
          formulario = AutosFormulario(request.POST)
          
          if formulario.is_valid():
               data = formulario.cleaned_data 
               autos = Autos(marca=data['marca'], modelo=data['modelo'], año=data['año'])
               autos.save()
               return redirect('ver_autos')               
          else:
               return render (request, 'mvt2/crear_auto.html', {'formulario': formulario})
               
     formulario = AutosFormulario()
     
     return render (request, 'mvt2/crear_auto.html', {'formulario': formulario})

def editar_auto (request, id):
     
     auto = Autos.objects.get(id=id)
     
     if request.method == 'POST':
          formulario = AutosFormulario(request.POST)

          if formulario.is_valid():               
               data = formulario.cleaned_data 
               auto.marca = data['marca']
               auto.modelo = data['modelo']
               auto.año = data['año']
               auto.save()
               return redirect('ver_autos')               

     formulario = AutosFormulario(initial={'marca':auto.marca, 'modelo':auto.modelo, 'año':auto.año})
     
     return render (request, 'mvt2/editar_auto.html', {'formulario': formulario, 'auto': auto})
               
               
def eliminar_auto(request,id):
     auto = Autos.objects.get(id=id)
     auto.delete()
     return redirect("ver_autos")


class ListaAutos(ListView):
     model = Autos
     template_name= "mvt2/ver_autos_cbv.html"
     
     
class CrearAuto(CreateView):
     model = Autos
     success_url = "/autos/"
     template_name = "mvt2/crear_auto_cbv.html"
     fields = ["marca","modelo","año"]

class EditarAuto(UpdateView):
     model = Autos
     success_url = "/autos/"
     template_name = "mvt2/editar_auto_cbv.html"
     fields = ["marca","modelo","año"]
     
class EliminarAutos(DeleteView):
     model = Autos
     success_url = "/autos/"
     template_name = "mvt2/eliminar_auto_cbv.html"
     
#class VerAutos(ListView):
