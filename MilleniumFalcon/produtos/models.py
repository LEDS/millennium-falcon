from django.db import models

class Atividade (models.Model):
    nome = models.CharField(max_length=255)
    
    tcc = 'TC'
    palestra = 'PA'
    minicur = 'MC'
    outro = 'OU'
    tipo_existentes = (
        (tcc, 'TCC'),
        (palestra, 'Palestra'),
        (minicur, 'Mini Curso'),
        (outro, 'Outro'),
    )
    tipo = models.CharField(max_length=2, choices= tipo_existentes)
    
    data = models.DateField()
    local = models.CharField(max_length=255, null=True)
    Descricao = models.TextField(null=True)
    
    def __str__(self):
        return self.nome