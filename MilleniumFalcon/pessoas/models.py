from django.db import models
from produtos.models import Atividade
from projetos.models import Projeto

class Membro (models.Model):

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
    estu = 'ES'
    prof = 'PR'
    tec = 'TE'
    out = 'OU'

    papeis_existentes = (
        (estu, 'Estudante'),
        (prof, 'Professor'),
        (tec, 'Tecnico'),
        (out, 'Outro'),
    )
    papel = models.CharField(
        max_length=2,
        choices= papeis_existentes,
        default= out,
    )
    nome = models.CharField(max_length=255)
    matricula = models.CharField(max_length=255)
    email = models.EmailField()
    lattes = models.CharField(max_length=255)

    nascimento = models.DateField()
    data_entrada = models.DateField()
    data_saida = models.DateField(null=True)

    formacao = models.ManyToManyField("Formacao")
    projeto = models.ManyToManyField("projetos.Projeto")
    atividade = models.ManyToManyField("produtos.Atividade")

    def __str__(self):
        return self.nome

class RedeSocial (models.Model):
    link = models.CharField(max_length=255)
    membro = models.ForeignKey(Membro, on_delete=models.CASCADE)
    def __str__(self):
        return self.link

class Formacao (models.Model):
    nome = models.CharField(max_length=255)
    instituicao = models.CharField(max_length=255)
    finalizado = models.BooleanField(default=1)

    def __str__(self):
        return self.nome
    
class Bolsa (models.Model):
    valor = models.FloatField()
    data_inicio = models.DateField(null=True)
    data_fim = models.DateField(null=True)
    projeto = models.ForeignKey(Projeto, on_delete=models.CASCADE)
    membro = models.ForeignKey(Membro, on_delete=models.CASCADE)