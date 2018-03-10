from django.db import models

class Projeto (models.Model):
    nome = models.CharField(max_length=255)
    data_inicio = models.DateField()
    data_fim = models.DateField()
    sobre = models.TextField()

    def __str__(self):
        return self.nome

class Fomento (models.Model):
    nome = models.CharField(max_length=255)
    projeto = models.ForeignKey(Projeto, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome

class Parceiro (modedef __str__(self):
        return self.nomels.Model):
    Nome = models.CharField(max_length=255)
    email = models.EmailField()
    telefone = models.CharField(max_length=255)
    detalhes = models.TextField()
    projeto = models.ManyToManyField("Projeto")
    projeto = models.ForeignKey(Projeto, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome