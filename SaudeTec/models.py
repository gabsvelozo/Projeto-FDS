from django.db import models

class Ficha_Pre_Consulta(models.Model):
    motivo = models.TextField(max_length=1000)
    periodo = models.CharField(max_length=1000)
    dor = models.IntegerField()
    quando_dor = models.TextField(max_length=50)
    algo_mais = models.TextField(max_length = 1000)
