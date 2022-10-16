from django.urls import path
from MVT_App import views

urlpatterns = [
    path("", views.index, name="index"),
    path('crear-personas/', views.crear_persona, name="crear_persona"),
    path('ver-personas/', views.ver_persona, name="ver_persona" ),
    path('about/', views.about, name="about" ),
]