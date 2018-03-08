from django.db import models

class Atividade (models.Model):
    nome = models.CharField(max_length=255)
    data = models.DateField()
    duracao = models.CharField(max_length=255)
    sobre = models.TextField()


class Projeto (models.Model):
    nome = models.CharField(max_length=255)
    data_inicio = models.DateField()
    data_fim = models.DateField()
    sobre = models.TextField()
    

class Fomento (models.Model):
    nome = models.CharField(max_length=255)
    projeto = models.ForeignKey(Projeto, on_delete=models.CASCADE)
class Parceiro (models.Model):
    Nome = models.CharField(max_length=255)
    email = models.EmailField()
    telefone = models.CharField(max_length=255)
    detalhes = models.TextField()
    projeto = models.ManyToManyField("Projeto")