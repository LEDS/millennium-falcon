from django.db import models

class Atividade (models.Model):
    nome = models.CharField(max_length=255)

class Projeto (models.Model):
    nome = models.CharField(max_length=255)

class Fomento (models.Model):
    nome = models.CharField(max_length=255)