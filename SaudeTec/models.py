from django.db import models

from django.db import models

class ficha_pre_consulta(models.Model):
    queixa_principal = models.TextField(max_length=1000)
    causa_da_queixa = models.TextField(max_length=1000)
    medida_de_tempo = models.CharField(max_length=50)
    duracao_sintomas = models.IntegerField(max_length=50)
    intensidade_da_dor = models.IntegerField()
    constancia_da_dor = models.TextField(max_length=50)
    agravantes_da_molestia = models.TextField(max_length = 1000)
