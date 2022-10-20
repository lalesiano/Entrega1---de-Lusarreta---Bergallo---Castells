from django.urls import path
from MVT_App_2 import views

urlpatterns = [
    path("ver-autos/", views.ver_autos, name="ver-autos"),
    path("crear-auto/", views.crear_auto, name="crear-auto"),
]