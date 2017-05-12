from django.contrib import admin
from .models import Pessoa, Professor, Servidor, Aluno, Representante_parceiro
admin.site.register(Pessoa)
admin.site.register(Professor)
admin.site.register(Servidor)
#admin.site.register(Alunos)
admin.site.register(Representante_parceiro)

class AlunoAdmin(admin.ModelAdmin):
  list_display = ['nome','papel','entrada_leds','periodo']
  list_filter = ['papel']

admin.site.register(Aluno,AlunoAdmin)