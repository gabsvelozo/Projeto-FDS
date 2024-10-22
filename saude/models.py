from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class HistoricoMedico(models.Model):
    nome = models.CharField(max_length=100, blank=False, default='Sem nome')
    idade = models.PositiveIntegerField(blank=False, default=0)
    medicacao = models.TextField(blank=True, default='Não usa medicamento')
    doencas = models.TextField(blank=True, default='Sem deonças pré-existentes')
    cirugias = models.TextField(blank=True, default='Sem cirugias')
    alergias = models.TextField(blank=True, default='Sem alergias')

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
    especialidade = models.ForeignKey('saude.especialidade', on_delete=models.CASCADE)
    local = models.ForeignKey(Local, on_delete=models.CASCADE)
    data = models.DateField()
    especialista = models.CharField(max_length=100)  

    def __str__(self):
        return f'{self.usuario.username} - {self.especialidade.nome} em {self.local.nome} na {self.data}'

class SintomasUsuario(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    sintomas = models.TextField()
    periodo = models.CharField(max_length=100, default='Desconhecido') 
    dor = models.IntegerField(default=0)
    quando_dor = models.CharField(max_length=50, default='Nunca')  
    algo_mais = models.TextField(blank=True, default='N/A')  
    created_at = models.DateTimeField(auto_now_add=True)  

    def __str__(self):
        return f"Sintomas de {self.usuario.username}"

    @classmethod    
    def get_consultas(cls):
        return cls.objects.all()
    
class Bairros(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

class Locais(models.Model):
    nome = models.CharField(max_length=100)
    bairro = models.ForeignKey(Bairros, on_delete=models.CASCADE)
    

    def __str__(self):
        return self.nome
    
class Info_local(models.Model):
    nome = models.TextField(blank=True, null=True)
    locais = models.ForeignKey(Locais, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return self.nome
    