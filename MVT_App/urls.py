from django.urls import path
from MVT_App import views

urlpatterns = [
    path("", views.index, name="index"),
    path('crear-personas/<str:nombre>/<str:apellido>/', views.crear_persona),
    path('ver-personas/', views.ver_persona, name="ver_persona" ),
]