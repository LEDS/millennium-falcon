from django.db import models

class Atividade (models.Model):
    nome = models.CharField(max_length=255)
    data = models.DateField()
    duracao = models.CharField(max_length=255)


class Projeto (models.Model):
    nome = models.CharField(max_length=255)
    data_inicio = models.DateField()
    data_fim = models.DateField()

class Fomento (models.Model):
    nome = models.CharField(max_length=255)

class Parceiro (models.Model):
    Nome = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    telefone = models.CharField(max_length=255)
    detalhes = models.CharField(max_length=255)
    projeto = models.ManyToManyField("Projeto")