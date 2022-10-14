from urllib import request
from django.shortcuts import render
from django.http import HttpResponse
from gestionPedidos_APP.models import Productos

# Create your views here.
def busqueda(request):
    return render(request, "busqueda_producto.html")

def buscar(request):
    if request.GET["prd"]:
       # mensaje = "Producto buscado: %r" %request.GET["prd"]
       producto = request.GET["prd"]
       if len(producto)>20:
            mensaje = "Texto de busqueda desmasiado largo"
       else:
            prod = Productos.objects.filter(nombre__icontains = producto)
            return render(request, "resultado.html", {"producto": prod, "query": producto})
    else:
        mensaje = "No has instroducido nada de nada"
    
    return HttpResponse(mensaje)