from django.shortcuts import render
from .forms import inscripcionForm
from .models import *

def index(request):
    inscripcion_form = inscripcionForm()
    competidores = Competidor.objects.order_by('id')


    if request.method == 'POST':
        inscripcion_form = inscripcionForm(request.POST)
        if inscripcion_form.is_valid():
            inscripcion_form.save()
            inscripcion_form = inscripcionForm()

    context = {
        'inscripcion_form': inscripcion_form,
        'competidores': competidores
    }
    
    return render(request, 'index.html', context)

