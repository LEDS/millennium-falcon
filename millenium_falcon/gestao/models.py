from __future__ import unicode_literals
from django.db import models

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

class Pessoa(models.Model):
    nome = models.CharField(max_length=255)
    papel = models.CharField(max_length=255)
    entrada_leds = models.DateField()
    saida_leds = models.DateField(blank=True, null=True)
    projeto_envolvido = models.ManyToManyField(Projeto)
    email = models.CharField(max_length=255, null=True)
    telefone = models.CharField(max_length=255, null=True)
    bolsa = models.ForeignKey("Bolsa",on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.nome

class Aluno(Pessoa):
    periodo_atual =  models.IntegerField()
    periodo_saida =  models.IntegerField(blank=True, null=True)
    data_nascimento = models.DateField(null=True)
    lattes = models.URLField(max_length=255, null=True)
    cpf = models.CharField(max_length=11,default="")
    habilidades = models.ManyToManyField("Habilidade")

class Professor(Pessoa):
    setor_vinculado = models.CharField(max_length=255, null=True)

class Servidor(Pessoa):
    setor_vinculado = models.CharField(max_length=255, null=True)


class Habilidade(models.Model):
    skill = models.CharField(max_length=255, unique=True)
    def __str__(self):
        return self.skill
