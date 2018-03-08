from django.contrib import admin
from .models import Atividade, Projeto, Fomento

admin.site.register(Atividade)
admin.site.register(Projeto)
admin.site.register(Fomento)