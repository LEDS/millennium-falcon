from django.contrib import admin

class ProjetoAdmin(admin.ModelAdmin):
    list_display = ['nome']
    list_filter = ['nome']
admin.site.register(Projeto,ProjetoAdmin)

class FomentoAdmin(admin.ModelAdmin):
    list_display = ['nome']
    list_filter = ['nome']
admin.site.register(Fomento,FomentoAdmin)