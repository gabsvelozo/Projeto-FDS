from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

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
