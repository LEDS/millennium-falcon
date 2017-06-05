from django.contrib import admin

# Register your models here.
from gestao.models import *
from pessoas.models import *
from institucional.models import *

class InstituicaoAdmin(admin.ModelAdmin):
    list_display = ['nome_instituto','endereco']
    list_filter = ['nome_instituto','endereco']
admin.site.register(Instituicao)

class CampusAdmin(admin.ModelAdmin):
    list_display = ['nome_campus','instituicao_vinculada']
    list_filter = ['nome_campus','instituicao_vinculada']
admin.site.register(Campus)

class SetorAdmin(admin.ModelAdmin):
    list_display = ['nome_setor','campus_vinculado']
    list_filter = ['nome_setor','campus_vinculado']
admin.site.register(Setor)

class CursoAdmin(admin.ModelAdmin):
    list_display = ['nome_curso','campus_vinculado']
    list_filter = ['nome_curso','campus_vinculado']
admin.site.register(Curso)
