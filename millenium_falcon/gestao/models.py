from __future__ import unicode_literals
from django.db import models

class Parceiro(models.Model):
    nome_parceiro = models.CharField(max_length=255)
    nome_representante = models.CharField(max_length=255)
    telefone = models.CharField(max_length=255)
    email = models.CharField(max_length=255)

class Projeto(models.Model):
    nome_projeto = models.CharField(max_length=255)
    data_inicio = models.DateField()
    data_fim = models.DateField()
    fomento = models.CharField(max_length=255)
    parceiro_envolvido = models.ForeignKey(Parceiro, on_delete=models.CASCADE, null=True)

class Pessoa(models.Model):
    nome = models.CharField(max_length=255,)
    papel = models.CharField(max_length=255)
    entrada_leds = models.DateField()
    saida_leds = models.DateField()
    projeto_envolvido = models.ForeignKey(Projeto, on_delete=models.CASCADE, null=True)

class Aluno(Pessoa):
    periodo =  models.IntegerField()
    status_bolsa = models.BooleanField(default=False)
    valor_bolsa = models.BooleanField(default=False)

class Professor(Pessoa):
    email = models.CharField(max_length=255)
    setor_vinculado = models.CharField(max_length=255, null=True)

class Servidor(Pessoa):
    email = models.CharField(max_length=255)
    setor_vinculado = models.CharField(max_length=255, null=True)