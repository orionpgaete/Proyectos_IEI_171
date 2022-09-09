from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'templatesWeb/index.html')

def plantillas(request):

    data = {"nombre": "Pedro", "apellido": "gaete"}
    return render(request, 'templatesWeb/miplantilla.html', data)


def usuario(request):
    data = {"id":"123",
            "nombre": "pedro gaete",
            "email": "pedro@pedro.cl"}

    return render(request, 'templatesWeb/userinfotemplates.html', data)