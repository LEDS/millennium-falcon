from __future__ import unicode_literals
from django.db import models
from gestao.models import *

# Create your models here.

class Habilidade(models.Model):
    skill = models.CharField(max_length=255, unique=True)
    def __str__(self):
        return self.skill

class Pessoa(models.Model):
    nome = models.CharField(max_length=255)
    entrada_leds = models.DateField()
    saida_leds = models.DateField(blank=True, null=True)
    email = models.CharField(max_length=255, null=True)
    telefone = models.CharField(max_length=255, null=True)
    bolsa = models.ForeignKey("gestao.Bolsa",blank=True, null=True)
    cpf = models.CharField("CPF",max_length=11,default="")
    habilidades = models.ManyToManyField("Habilidade")
    lattes = models.URLField(max_length=255, null=True)
    def __str__(self):
        return self.nome

class Aluno(Pessoa):
    periodo_atual = models.IntegerField()
    periodo_saida = models.IntegerField(blank=True, null=True)
    data_nascimento = models.DateField(null=True)
    banco = models.CharField(max_length=255,blank=True, null=True)
    numero_conta = models.CharField(max_length=255,blank=True, null=True)
    agencia = models.CharField(max_length=255,blank=True, null=True)
    curso = models.ForeignKey("institucional.Instituicao",blank=True, null=True)


class Professor(Pessoa):
    setor_vinculado = models.ForeignKey("institucional.Setor",blank=True, null=True)
    siape = models.CharField(max_length=255, null=True)

class Servidor(Pessoa):
    setor_vinculado = models.ForeignKey("institucional.Setor",blank=True, null=True)
    siape = models.CharField(max_length=255, null=True)
