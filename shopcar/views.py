from django.shortcuts import render,redirect
from .carro import Carro
from tienda.models import Producto

# Create your views here.
def agregar_producto(request,producto_id):
    carro=Carro(request)
    producto=Producto.objects.get(id=producto_id)
    carro.agregar(producto=producto)
    return redirect("/")

def eliminar_producto(request,producto_id):
    carro=Carro(request)
    producto=Producto.objects.get(id=producto_id)
    carro.eliminar(producto=producto)
    return redirect("carro:ver_carro")

def restar_producto(request,producto_id):
    carro=Carro(request)
    producto=Producto.objects.get(id=producto_id)
    carro.restar(producto=producto)
    return redirect("carro:ver_carro")

def sumar_producto(request,producto_id):
    carro=Carro(request)
    producto=Producto.objects.get(id=producto_id)
    carro.sumar(producto=producto)
    return redirect("carro:ver_carro")


def limpiar_carro(request):
    carro=Carro(request)
    carro.limpiar_carro()
    return redirect("carro:ver_carro")

def ver_carro(request):
    return render(request,"carro/car_detail.html")
