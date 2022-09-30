from urllib import request
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def busqueda(request):
    return render(request, "busqueda_producto.html")

def buscar(request):
    mensaje = "Producto buscado: %r" %request.GET["prd"]
    return HttpResponse(mensaje)