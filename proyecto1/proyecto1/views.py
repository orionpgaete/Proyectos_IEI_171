from datetime import datetime
from django.http import HttpResponse

import datetime

docu = """<html>
            <body>
                <h1>Hola alumnos de la clase Django San Viernes</h1>
            </body>
        </html>"""


def saludo(request):
    return HttpResponse(docu)

def despedida(request):
    return HttpResponse("Chaoolin Beibe !!!!")

def muestrafecha(request):
    fecha_actual = datetime.datetime.now()
    return HttpResponse("""<html>
                            <body>
                                <h2>Fecha y Hora actual %s</h2>
                            </body>
                        </html>""" %fecha_actual)

def calcularEdad(request, agno, edad):
    #edadactual = 18
    periodo = agno - 2022
    edadfutura = edad + periodo

    return HttpResponse("""<html>
                            <body>
                                <h2>En el año %s tendras %s años.</h2>
                            </body>
                        </html>""" %(agno, edadfutura))
