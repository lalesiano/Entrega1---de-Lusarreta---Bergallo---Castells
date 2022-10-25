
from MVT_App_2.models import Autos
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

class ListaAutos(ListView):
     model = Autos
     template_name= "mvt2/ver_autos_cbv.html"
          
class CrearAuto(CreateView):
     model = Autos
     success_url = "/autos/"
     template_name = "mvt2/crear_auto_cbv.html"
     fields = ["marca","modelo","año"]

class EditarAuto(LoginRequiredMixin, UpdateView):
     model = Autos
     success_url = "/autos/"
     template_name = "mvt2/editar_auto_cbv.html"
     fields = ["marca","modelo","año"]
     
class EliminarAutos(LoginRequiredMixin, DeleteView):
     model = Autos
     success_url = "/autos/"
     template_name = "mvt2/eliminar_auto_cbv.html"
     
#class VerAutos(ListView):
