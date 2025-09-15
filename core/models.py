from django.db import models
class alunos(models.Model):
    nome = models.CharField(max_length=50) 
    turma = models.CharField(max_length=50)
    sala = models.CharField(max_length=50)
    idade = models.IntegerField()
  
    def __str__ (self):
        return self.nome + "da" + self.sala