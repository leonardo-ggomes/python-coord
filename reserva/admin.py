from django.contrib import admin
from .models import Docente, Turma, Ambiente


admin.site.site_header = "Coordenação"
admin.site.site_title = "Coordenação"
admin.site.site_url = "/painel"

# Register your models here.

class DocenteAdmin(admin.ModelAdmin):
    list_display = ("nome","sobrenome") 

admin.site.register(Docente, DocenteAdmin)

admin.site.register(Turma)
admin.site.register(Ambiente)