# app/models.py

from django.db import models
from django.contrib.auth.models import User

class Especialidade(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

class Local(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

class Consulta(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    especialidade = models.ForeignKey(Especialidade, on_delete=models.CASCADE)
    local = models.ForeignKey(Local, on_delete=models.CASCADE)
    data = models.DateField()
    especialista = models.CharField(max_length=100)  # Caso queira armazenar o nome do especialista

    def __str__(self):
        return f'{self.usuario.username} - {self.especialidade.nome} em {self.local.nome} na {self.data}'
