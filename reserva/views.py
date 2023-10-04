from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .forms import EventoForm

def eventos(request):
    
    forms = EventoForm()
    
    context = {       
        'form': forms
    }
    
    if request.method == 'POST':
            
        forms = EventoForm(request.POST)
            
        if forms.is_valid():
            forms.save()
            HttpResponseRedirect("painel")
            
        else:
            forms = EventoForm()
    
    return HttpResponse(render(request, "painel.html", context))

