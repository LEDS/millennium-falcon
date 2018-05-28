from django.contrib import admin
from .models import Projeto, Fomento, Parceiro

class ProjetoAdmin(admin.ModelAdmin):
    list_display = ['nome']
    list_filter = ['nome']
admin.site.register(Projeto,ProjetoAdmin)

class FomentoAdmin(admin.ModelAdmin):
    list_display = ['nome']
    list_filter = ['nome']
admin.site.register(Fomento,FomentoAdmin)


admin.site.register(Parceiro)