from django.contrib import admin
from pessoas.models import *
# Register your models here.


admin.site.register(Habilidade)

class AlunoAdmin(admin.ModelAdmin):
    list_display = ['nome','papel','lattes','periodo_atual']
    list_filter = ['papel','periodo_atual','habilidades']
admin.site.register(Aluno)

#class ProfessorAdmin(admin.ModelAdmin):
admin.site.register(Professor)

#class ServidorAdmin(admin.MoedelAdmin):
admin.site.register(Servidor)
