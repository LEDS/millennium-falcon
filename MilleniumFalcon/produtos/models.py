from django.db import models

class Atividade (models.Model):
    nome = models.CharField(max_length=255)
    data = models.DateField()
    duracao = models.CharField(max_length=255)
    sobre = models.TextField()
    
    def __str__(self):
        return self.nome