from django.db import models

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
         ('#70a288b0','Verde'),
         ('#dab785b0','Amarelo'),
         ('#d5896fb0','Vermelho'),
    )
    
    inicio = models.TimeField()
    fim = models.TimeField()
    docente = models.ForeignKey(Docente, on_delete=models.DO_NOTHING)
    turma = models.ForeignKey(Turma, on_delete=models.DO_NOTHING)
    etiqueta = models.CharField(max_length=50, choices=EIQUETA, default='Verde')
    ambiente = models.ForeignKey(Ambiente, on_delete=models.DO_NOTHING)
    diasemana = models.CharField(max_length=20, choices=SEMANA, default='Segunda')