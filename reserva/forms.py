from django import forms
from django.forms import widgets
from .models import Evento

class EventoForm(forms.ModelForm):  
           
    class Meta:
        model = Evento
        
        fields = [
            'inicio',
            'fim',
            'docente',
            'turma',
            'ambiente',
            'etiqueta',
            'diasemana'
        ]
    
    def __init__(self, *args, **kwargs):
        super(EventoForm, self).__init__(*args, **kwargs)
        
        self.fields['inicio'].widget = forms.TimeInput(attrs={'type':'time','class':'cal-sel-timeStart', 'id':'cal-timeStart'})
        self.fields['inicio'].input_formats= ['%H:%M']
        self.fields['fim'].widget = forms.TimeInput(attrs={'type':'time','class':'cal-sel-timeEnd', 'id':'cal-timeEnd'})
        self.fields['fim'].input_formats= ['%H:%M']
        self.fields['diasemana'].label ="Dia da Semana"

    
