from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def index(request):
    return render(request, 'publica/index.html')

def nosotros(request):
    return render(request, 'publica/nosotros.html')

def contacto(request):
    return render(request, 'publica/contacto.html')

def productos(request):
    return render(request, 'publica/productos.html')