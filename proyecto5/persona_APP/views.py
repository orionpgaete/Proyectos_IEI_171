from django.shortcuts import render
from persona_APP.models import Persona

# Create your views here.
def persona(request):
    persona = Persona.objects.all()
    data = {'persona' : persona}
    return render(request, 'persona.html', data)