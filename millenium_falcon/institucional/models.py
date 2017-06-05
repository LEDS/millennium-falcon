from __future__ import unicode_literals
from django.db import models
# Create your models here.

class Instituicao(models.Model):
    nome_instituto = models.CharField(max_length=255)
    endereco = models.CharField(max_length=255)

class Campus(models.Model):
    nome_campus = models.CharField(max_length=255)
    instituicao_vinculada = models.ForeignKey("Instituicao", null=True, blank=True)

class Setor(models.Model):
    nome_setor = models.CharField(max_length=255)
    campus_vinculado = models.ForeignKey("Campus", null=True, blank=True)

class Curso(models.Model):
    nome_curso = models.CharField(max_length=255)
    campus_vinculado = models.ForeignKey("Campus", null=True, blank=True)
