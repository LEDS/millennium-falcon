from django.db import models

class Jedi (models.Model):
    nivel = 
    nome = models.CharField(max_length=200)
    matricula = models.CharField(max_length=200)

    curso = 
    
    nascimento = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    lattes = models.CharField(max_length=200)
    data_entrada = models.CharField(max_length=200)
    data_saida = models.CharField(max_length=200)

    formacao = 
    social = 

    projeto = 
    atividade = 

class Nivel (models.Model):
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


class Social (models.Model):
    nome = models.CharField(max_length=200)
    link = models.CharField(max_length=200)

class Formacao (models.Model):
    nome = models.CharField(max_length=200)

class Curso (models.Model):
    nome = models.CharField(max_length=200)
    instituicao = models.CharField(max_length=200)
