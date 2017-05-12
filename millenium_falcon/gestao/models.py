from __future__ import unicode_literals
from django.db import models

class Pessoa(models.Model):
    nome = models.CharField(max_length=255, null=False)
    papel = models.CharField(max_length=255, null=False)
    entrada_leds = models.DateField()
    saida_leds = models.DateField()

class Professor(Pessoa):
    email = models.CharField(max_length=255, null=False)


class Servidor(Pessoa):
    email = models.CharField(max_length=255, null=False)

class Aluno(Pessoa):
    periodo =  models.IntegerField()
    status_bolsa = models.BooleanField(default=False)
    valor_bolsa = models.BooleanField(default=False)

class Representante_parceiro(Pessoa):
    email = models.CharField(max_length=255, null=False)
    telefone = models.CharField(max_length=255, null=False)

class Projeto(models.Model):
    nome_projeto = models.CharField(max_length=255, null=False)
    data_inicio = models.DateField()
    data_fim = models.DateField()
    fomento = models.CharField(max_length=255, null=False)
    