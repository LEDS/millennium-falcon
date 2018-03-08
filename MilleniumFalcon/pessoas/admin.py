from django.contrib import admin
from .models import Jedi, Social, Formacao, Curso

class JediAdmin(admin.ModelAdmin):
    list_display = ['nome']
    list_filter = ['nome']
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
    list_display = ['nome']
    list_filter = ['nome']
admin.site.register(Curso,CursoAdmin)
