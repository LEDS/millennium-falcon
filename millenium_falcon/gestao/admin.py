from django.contrib import admin
#from .models import Pessoa, Professor, Servidor, Aluno, Representante_parceiro
#Lista logo após o model todas as classes que quer mandar par ao admin
from .models import *

#class ParceiroAdmin(admin.ModelAdmin):
admin.site.register(Parceiro)

#class PessoaAdmin(admin.ModelAdmin):
#admin.site.register(Pessoa)

#class ProfessorAdmin(admin.ModelAdmin):
admin.site.register(Professor)

#class ServidorAdmin(admin.MoedelAdmin):
admin.site.register(Servidor)

#class ProjetoAdmin(admin.ModelAdmin):
admin.site.register(Projeto)

class AlunoAdmin(admin.ModelAdmin):
    list_display = ['nome','papel','entrada_leds','periodo_atual']
    list_filter = ['papel','periodo_atual','projeto_envolvido','habilidades']



admin.site.register(Aluno,AlunoAdmin)




admin.site.register(Bolsa)
admin.site.register(Fomento)

admin.site.register(Alocacao_bolsa)
admin.site.register(Habilidade)
