from django.urls import path
from MVT_App_2 import views

urlpatterns = [
    path("hola/", views.hola, name="hola"),
]