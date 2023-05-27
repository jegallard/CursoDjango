from django.shortcuts import render
from django.http import HttpResponse
from .forms import contacto_form

# Create your views here.

def index(request):
    return render(request, 'publica/index.html')

def nosotros(request):
    return render(request, 'publica/nosotros.html')

def productos(request):
    listado_productos = [
        {
            "titulo" : "Planta 1",
            "imagen" : "{% static './publica/img/planta8.avif' %}",
            "precio" : 1000
        },
        {
            "titulo" : "Planta 2",
            "imagen" : "{% static './publica/img/planta8.avif' %}",
            "precio" : 1000
        },
        {
            "titulo" : "Planta 3",
            "imagen" : "{% static './publica/img/plantafb.jpg' %}",
            "precio" : 1000
        },
        {
            "titulo" : "Planta 4",
            "imagen" : "{% static './publica/img/planta8.avif' %}",
            "precio" : 1000
        },
        {
            "titulo" : "Planta 5",
            "imagen" : "{% static './publica/img/planta8.jpg' %}",
            "precio" : 1000
        },
    ]
    
    return render(request, 'publica/productos.html', {"productos":listado_productos})

def contacto(request):
    mensaje = None #Ver clase 17
    #Si recibe la URL por POST toma los datos del formulario
    if request.method == "POST":
        formContacto = contacto_form(request.POST)
        #Se valida los datos is_valid()
        if formContacto.is_valid():
            pass
            #messages.info(request,"!Aviso")        
        else:
          formContacto = contacto_form() 
    #Si la URL es recibida por el metodo GET crea un formulario en blanco (sin datos)
    else:
        formContacto = contacto_form()
    return render(request, "publica/contacto.html", {"form": formContacto})
    

