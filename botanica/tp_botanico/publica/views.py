from django.shortcuts import render
from django.http import HttpResponse
from .forms import contacto_form

# Create your views here.

def index(request):
    return render(request, 'publica/index.html')

def nosotros(request):
    return render(request, 'publica/nosotros.html')

def productos(request):
    return render(request, 'publica/productos.html')

def contacto(request):
    if request.method == "POST":
        # create a form instance and populate it with data from the request:
        form = contacto_form(request.POST)
        return HttpResponse("<h1>Perfecto</h1>")
        # check whether it's valid:
        #if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            #return HttpResponseRedirect("/thanks/")
    # if a GET (or any other method) we'll create a blank form
    else:
        form = contacto_form()
    return render(request, "publica/contacto.html", {"form": form})
    

