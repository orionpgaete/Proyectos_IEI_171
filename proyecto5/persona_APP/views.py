from django.shortcuts import render
from persona_APP.models import Persona, Proyecto

# Create your views here.
def persona(request):
    per  = Persona.objects.all()
    data = {'persona' : per}
    return render(request, 'persona.html', data)

def index(request):
    return render(request, 'index.html')

def listaproyecto(request):
    pro = Proyecto.objects.all()
    data = {'proyecto': pro}
    return render(request, 'listadoproyecto.html', data)

