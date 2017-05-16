from __future__ import unicode_literals
from django.db import models
from pessoas.models import *

class Parceiro(models.Model):
    #Na verdade é o Cliente com nome mais bonito
    nome_parceiro = models.CharField(max_length=255)
    nome_representante = models.CharField(max_length=255)
    telefone = models.CharField(max_length=255)
    email = models.CharField(max_length=255, null=True)
    cnpj = models.CharField(max_length=255, null=True)

    def __str__(self):
        return self.nome_parceiro

class Projeto(models.Model):
    nome_projeto = models.CharField(max_length=255)
    data_inicio = models.DateField()
    data_fim = models.DateField(blank=True, null=True)
    parceiro_envolvido = models.ForeignKey(Parceiro, on_delete=models.CASCADE, null=True)
    pessoas_envolvidas = models.ManyToManyField("Pessoa")
    def __str__(self):
        return self.nome_projeto

class Fomento(models.Model):
    nome = models.CharField(max_length=255)
    parceiro = models.ForeignKey("Parceiro", on_delete=models.CASCADE)

    def __str__(self):
        return self.nome

class Bolsa(models.Model):
    nome_bolsa = models.CharField(max_length=255, blank=True)
    fomento = models.ForeignKey("Fomento", on_delete=models.CASCADE)
    valor_bolsa = models.IntegerField(default=0)
    projeto = models.ForeignKey("Projeto", on_delete=models.CASCADE)

    def __str__(self):
        return self.nome_bolsa

class Alocacao_bolsa(models.Model):
    bolsa = models.ForeignKey("Bolsa", null=True)
    inicio = models.DateField(null=True)
    fim = models.DateField(null=True)
    pessoa = models.ForeignKey("Pessoa", null=True)

class Habilidade(models.Model):
    skill = models.CharField(max_length=255, unique=True)
    def __str__(self):
        return self.skill
