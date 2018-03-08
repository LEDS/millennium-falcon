from django.db import models
from produtos.models import Atividade, Projeto

class Jedi (models.Model):

    youngling = 'YL'
    padawan = 'PW'
    jedi = 'JD'
    mestre = 'MJ'

    niveis_existentes = (
        (youngling, 'Young ling'),
        (padawan, 'Padawan'),
        (jedi, 'Jedi'),
        (mestre, 'Mestre Jedi'),
    )
    nivel = models.CharField(
        max_length=2,
        choices= niveis_existentes,
        default=youngling,
    )

    nome = models.CharField(max_length=255)
    matricula = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    lattes = models.CharField(max_length=255)

    curso = models.ManyToManyField("Curso")

    nascimento = models.DateField()
    data_entrada = models.DateField()
    data_saida = models.DateField()

    formacao = models.ManyToManyField("Formacao")
    social = models.ManyToManyField("Social")

    projeto = models.ManyToManyField("produtos.Projeto")
    atividade = models.ManyToManyField("produtos.Atividade")

class Social (models.Model):
    nome = models.CharField(max_length=255)
    link = models.CharField(max_length=255)

class Formacao (models.Model):
    nome = models.CharField(max_length=255)

class Curso (models.Model):
    nome = models.CharField(max_length=255)
    instituicao = models.CharField(max_length=255)
