from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Evento
from .forms import EventoForm
import json

def eventos(request):
    
    eventos = Evento.objects.select_related('turma','docente','ambiente').all()
    
    data = []
    
    forms = EventoForm()
    
    for item in eventos:
        data.append({
            'codigo' : item.pk,  
            'inicio' : str(item.inicio),
            'fim' : str(item.fim),
            'docente'  : item.docente.nome,
            'turma'  : item.turma.nome,
            'etiqueta'  : item.etiqueta,
            'ambiente'  : item.ambiente.nome,
            'diasemana' : item.diasemana,
            'codAmbiente': item.ambiente.pk
        })   
       
    context = {       
        'form': forms,
        'eventos':  json.dumps(data)
    }
    
    if request.method == 'POST':
            
        forms = EventoForm(request.POST)
            
        if forms.is_valid():
            forms.save()
            return HttpResponseRedirect("/painel/")
            
        else:
            forms = EventoForm() 
    elif  request.method == 'DELETE': 
        
        paramId = request.GET.get("id")              
        item = Evento.objects.filter(id=paramId)
        print(item)
        item.delete()
        
        return HttpResponse(status=200)
        
             
   
    
    return render(request, "painel.html", context)

