from __future__ import unicode_literals
from django.db import models
from pessoas.models import *
from institucional.models import *

class Projeto(models.Model):
    nome_projeto = models.CharField(max_length=255)
    data_inicio = models.DateField()
    data_fim = models.DateField(blank=True, null=True)
    parceiro_envolvido = models.ForeignKey("Parceiro", null=True)
    alunos_envolvidas = models.ManyToManyField("pessoas.Aluno",blank=True)
    professor_envolvidas = models.ManyToManyField("pessoas.Professor",blank=True)
    def __str__(self):
        return self.nome_projeto

class Representante(models.Model):
    nome = models.CharField(max_length=255)
    email = models.CharField(max_length=255, null=True)
    telefone = models.CharField(max_length=255, null=True)
    funcao = models.CharField(max_length=255, null=True)

class Parceiro(models.Model):
    #Na verdade é o Cliente com nome mais bonito
    nome_parceiro = models.CharField(max_length=255)
    nome_representante = models.ForeignKey("Representante",blank=True, null=True)
    telefone = models.CharField(max_length=255)
    email = models.CharField(max_length=255, null=True)
    cnpj = models.CharField(max_length=255, null=True)

    def __str__(self):
        return self.nome_parceiro

class Fomento(models.Model):
    nome = models.CharField(max_length=255)
    parceiro = models.ForeignKey("Parceiro",blank=True, null=True)

    def __str__(self):
        return self.nome

class Bolsa(models.Model):
    nome_bolsa = models.CharField(max_length=255, blank=True)
    fomento = models.ForeignKey("Fomento",blank=True, null=True)
    valor_bolsa = models.IntegerField(default=0)

    def __str__(self):
        return self.nome_bolsa
