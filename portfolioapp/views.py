"""
Autor: Luis Ramos (@luisAngelDev)
GitHub: https://github.com/luisAngelDev
Descripción: Vista de servicios para la pagina web personal.
"""
from django.shortcuts import render
from .models import Servicio

# Create your views here.

def home(request):
    servicios = Servicio.objects.all()
    return render(request, 'portfolioapp/home.html', {
        'servicios': servicios
        })

