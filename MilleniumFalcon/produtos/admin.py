from django.contrib import admin
from .models import Atividade, Projeto, Fomento, Parceiro


class AtividadeAdmin(admin.ModelAdmin):
    list_display = ['nome']
    list_filter = ['nome']
admin.site.register(Atividade,AtividadeAdmin)

