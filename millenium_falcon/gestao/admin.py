from django.contrib import admin
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
  list_display = ['nome','papel','entrada_leds','periodo']
  list_filter = ['papel']

admin.site.register(Aluno,AlunoAdmin)