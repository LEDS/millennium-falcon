from django.contrib import admin

# Register your models here.
from institucional.models import *
from pessoas.models import *

admin.site.register(Habilidade)

class AlunoAdmin(admin.ModelAdmin):
    list_display = ['nome','lattes','periodo_atual']
    list_filter = ['papel','periodo_atual','habilidades']
admin.site.register(Aluno)

class ProfessorAdmin(admin.ModelAdmin):
    list_display = ['nome','lattes','setor_vinculado']
    list_display = []

admin.site.register(Professor)

class ServidorAdmin(admin.ModelAdmin):
    list_display = ['nome','lattes','setor_vinculado']
    list_display = []

admin.site.register(Servidor)
