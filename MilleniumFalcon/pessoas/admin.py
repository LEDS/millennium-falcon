from django.contrib import admin
from .models import Membro, RedeSocial, Formacao

class MembroAdmin(admin.ModelAdmin):
    list_display = ['nome', 'nivel','papel']
    list_filter = ['nome', 'nivel','papel']
admin.site.register(Membro, MembroAdmin)


class FormaAdmin(admin.ModelAdmin):
    list_display = ['nome']
    list_filter = ['nome']
admin.site.register(Formacao,FormaAdmin)

admin.site.register(RedeSocial)