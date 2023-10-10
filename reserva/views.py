from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from .models import Evento
from .forms import EventoForm
import json

#@login_required
def eventos(request):    
 
    eventos = Evento.objects.select_related('turma','docente','ambiente').all()
    msg = "Atualizado!"
    data = []        
    forms = EventoForm()
    context = None
        
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
                   msg = "Salvo com sucesso!"
                   forms = EventoForm()
                   eventos = Evento.objects.select_related('turma','docente','ambiente').all()
            else:
                msg = "Já existe reserva neste período"
                            
        else:
            forms = EventoForm() 
    elif  request.method == 'DELETE': 
        
        try:
            paramId = request.GET.get("id")              
            item = Evento.objects.filter(id=paramId)            
            item.delete()          
            return HttpResponse(status=200)
        except:        
            return HttpResponse(status=500)
    
    
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
        'msg': msg 
    } 
   
    
    return render(request, "painel.html", context)




def analise(request):
    
    data = []
    
    eventos =  eventos = Evento.objects.select_related('turma','docente','ambiente').all()
    
    for item in eventos:
        
        data.append({
            'Inicio' : str(item.inicio),
            'Termino' : str(item.fim),
            'Docente'  : item.docente.nome,
            'Turma'  : item.turma.nome,
            'Ambiente'  : item.ambiente.nome,
            'Dia_Semana' : item.diasemana,
            'Aulas': item.aulas(),
            'Duracao': item.duracao()
        })   
       
    
    context = {
     'eventos': json.dumps(data) 
    }
    
    return render(request, "pivot.html", context)

