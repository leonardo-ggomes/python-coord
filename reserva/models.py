from django.db import models
from datetime import datetime

class Docente(models.Model):
    nome = models.CharField(max_length=50)
    sobrenome = models.CharField(max_length=50)
    
    def __str__(self):
        return f'{self.nome} {self.sobrenome}'
        
    
class Turma(models.Model):
    nome = models.CharField(max_length=50)
    descricao = models.CharField(max_length=255, null=True)
    
    def __str__(self):
        return f'{self.nome}'
    

class Ambiente(models.Model):
    nome = models.CharField(max_length=50)
    
    def __str__(self):
        return f'{self.nome}'
    

class Evento(models.Model):
    
    SEMANA = (
        ('Segunda','Segunda'),
        ('Terça','Terça'),
        ('Quarta','Quarta'),
        ('Quinta','Quinta'),
        ('Sexta','Sexta'),
        ('Sábado','Sábado'),
    )
    
    EIQUETA = (
         ('#70a288','Verde'),
         ('#dab785','Amarelo'),
         ('#d5896f','Vermelho'),
    )
    
    inicio = models.TimeField()
    fim = models.TimeField()
    docente = models.ForeignKey(Docente, on_delete=models.CASCADE)
    turma = models.ForeignKey(Turma, on_delete=models.CASCADE)
    etiqueta = models.CharField(max_length=50, choices=EIQUETA, default='Verde')
    ambiente = models.ForeignKey(Ambiente, on_delete=models.CASCADE)
    diasemana = models.CharField(max_length=20, choices=SEMANA, default='Segunda')
    
    
    def aulas(self):
        
        minAula = 45
        
        inicio = str(self.inicio).split(":") 
        fim = str(self.fim).split(":")    
        
        diferenceHour = int(fim[0]) - int(inicio[0])      
        
        totalAulas = (((diferenceHour * 60) - int(inicio[1])) + int(fim[1])) / minAula
            
        return round(totalAulas)
    
    
    def duracao(self):        
        inicio_minuto = self.inicio.hour * 60 + self.inicio.minute
        fim_minuto = self.fim.hour * 60 + self.fim.minute
        
        diferenca = (fim_minuto - inicio_minuto) / 60
     
        dif_hora = str(diferenca).split(".")[0]
        dif_min = int(str(diferenca).split(".")[1]) * 60
       
        return f'{dif_hora}.{dif_min}'
    
    
        
        