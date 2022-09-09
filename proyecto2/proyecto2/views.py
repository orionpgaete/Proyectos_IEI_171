from datetime import datetime
from django.http import HttpResponse
from django.template import Template, Context
import datetime

class Persona(object):
    def __init__(self, nombre, apellido) :
        self.nombre = nombre
        self.apellido = apellido

def web(request):
    #nombre = "Pedro"
    #apellido = "Gaete"

    p1 = Persona("Prof. Pedro", "Gaete")

    fecha = datetime.datetime.now()
    doc_externo = open("D:/1. Clases INACAP/2. Clases/2.31 Programacion Back-End/Proyectos-IEI-171/proyecto2/proyecto2/web/miplantilla.html")

    plantilla=Template(doc_externo.read())

    doc_externo.close()

    cont = Context({"nom_persona":p1.nombre, "apel_persona":p1.apellido, "fecha_actual": fecha, "temas":["Plantillas", "Modelos", "Formulario", "Vistas"]})

    docu = plantilla.render(cont)

    return HttpResponse(docu)