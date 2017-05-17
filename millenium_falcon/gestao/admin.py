from django.contrib import admin
#from .models import Pessoa, Professor, Servidor, Aluno, Representante_parceiro
#Lista logo após o model todas as classes que quer mandar par ao admin
from gestao.models import *


#class ProjetoAdmin(admin.ModelAdmin):
admin.site.register(Projeto)


#class ParceiroAdmin(admin.ModelAdmin):
admin.site.register(Parceiro)
admin.site.register(Representante)
admin.site.register(Fomento)
admin.site.register(Bolsa)
