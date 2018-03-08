from django.contrib import admin
from .models import Jedi, Social, Formacao, Curso

class JediAdmin(admin.ModelAdmin):
    list_display = ['nome', 'nivel']
    list_filter = ['nome', 'nivel']
admin.site.register(Jedi, JediAdmin)

class SocialAdmin(admin.ModelAdmin):
    list_display = ['nome']
    list_filter = ['nome']
admin.site.register(Social,SocialAdmin)

class FormaAdmin(admin.ModelAdmin):
    list_display = ['nome']
    list_filter = ['nome']
admin.site.register(Formacao,FormaAdmin)

class CursoAdmin(admin.ModelAdmin):
    list_display = ['nome', 'instituicao']
    list_filter = ['nome', 'instituicao']
admin.site.register(Curso,CursoAdmin)
