from django.urls import path
from MVT_App_2 import views

urlpatterns = [
 path("autos/", views.ListaAutos.as_view(), name="ver_autos"),
 path("autos/crear/", views.CrearAuto.as_view(), name="crear_auto"),
 path("autos/editar/<int:pk>", views.EditarAuto.as_view(), name="editar_auto"),
 path("autos/eliminar/<int:pk>", views.EliminarAutos.as_view(), name="eliminar_auto"),
]
