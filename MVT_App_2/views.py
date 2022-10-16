from datetime import datetime
from django.shortcuts import render, redirect
import random

def hola(request):
     return render(request,"hola.html")