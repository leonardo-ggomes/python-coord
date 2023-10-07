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
        'eventos':  json.dumps(data),
        'msg':''
    }
    
    if request.method == 'POST':
            
        forms = EventoForm(request.POST)
            
        if forms.is_valid():                      
      
            if not Evento.objects.filter(
                    ambiente_id=forms.data['ambiente'],
                    diasemana=forms.data['diasemana'],
                    inicio__lt=forms.data['fim'],
                    fim__gt=forms.data['inicio']
                ).exclude(inicio=forms.data['fim']).exists():                   
                   forms.save()
                   context['msg'] = "Salvo com sucesso!"
                   eventos = Evento.objects.select_related('turma','docente','ambiente').all()
            else:
                context['msg'] = "Já existe reserva neste período"
         
            #return render(request, "painel.html", context)
            #return HttpResponseRedirect("/painel/")          
          
            
        else:
            forms = EventoForm() 
    elif  request.method == 'DELETE': 
        
        try:
            paramId = request.GET.get("id")              
            item = Evento.objects.filter(id=paramId)            
            item.delete()
            context['msg'] = "Excluído com sucesso!"
            return HttpResponse(status=200)
        except:
            context['msg'] = "Erro 500!"
            return HttpResponse(status=500)
        
             
   
    
    return render(request, "painel.html", context)

