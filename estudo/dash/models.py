from django.db import models

class Matéria(models.Model):
    nome = models.CharField(max_length=100)
    descrição = models.TextField()

    def __str__(self):
        return self.nome

class Assunto(models.Model):
    nome = models.CharField(max_length=100)
    descrição = models.TextField()
    matéria = models.ForeignKey(Matéria, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome
