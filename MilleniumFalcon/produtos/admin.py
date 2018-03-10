from django.contrib import admin
from .models import Atividade


class AtividadeAdmin(admin.ModelAdmin):
    list_display = ['nome','tipo' , 'local', 'data']
    list_filter = ['tipo','local', 'data']
admin.site.register(Atividade,AtividadeAdmin)

