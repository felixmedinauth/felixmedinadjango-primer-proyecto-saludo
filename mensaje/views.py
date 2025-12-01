from django.shortcuts import render
from .models import Saludo

def saludo(request):
    saludos = Saludo.objects.all().order_by('-id') # Muestra los últimos primero
    return render(request, 'saludos/saludo.html', {'saludos': saludos})