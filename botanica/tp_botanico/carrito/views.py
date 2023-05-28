from django.shortcuts import render
from .carrito import Carrito
from publica.models import Producto
from django.shortcuts import redirect

# Create your views here.
def agregar_producto(request, producto_id):
    carrito = Carrito(request)
    producto = Producto.objects.get(id=producto_id)
    carrito.agregar(producto=producto)
    return redirect("publica/productos.html")

def eliminar_producto(request, producto_id):
    carrito = Carrito(request)
    producto = Producto.objects.get(id=producto_id)
    carrito.eliminar(producto=producto)
    return redirect("publica/productos.html")

def restar_producto(request, producto_id):
    carrito = Carrito(request)
    producto = Producto.objects.get(id=producto_id)
    carrito.restar(producto=producto)
    return redirect("publica/productos.html")

def limpiar_carrito(request, producto_id):
    carrito = Carrito(request)
    carrito.limpiar()
    return redirect("publica/productos.html")
    
