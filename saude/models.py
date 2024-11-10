from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


# Tabela no banco de dados que armazena informações sobre o histórico médico de uma pessoa
class HistoricoMedico(models.Model):
    nome = models.CharField(max_length=100, blank=False, default='Sem nome', null=False)
    idade = models.PositiveIntegerField(blank=False, default=0, null=False)
    medicacao = models.TextField(blank=True, default='Não usa medicamento', null=True)
    doencas = models.TextField(blank=True, default='Sem doenças pré-existentes', null=True)
    cirugias = models.TextField(blank=True, default='Sem cirurgias', null=True)
    alergias = models.TextField(blank=True, default='Sem alergias', null=True)


# Especialidades médicas disponíveis para agendamento de consultas
class Especialidade(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome


# Locais onde consultas médicas podem ser agendadas
class Local(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome


# Representa o agendamento de uma consulta médica no sistema
class Consulta(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    especialidade = models.ForeignKey('saude.especialidade', on_delete=models.CASCADE)
    local = models.ForeignKey(Local, on_delete=models.CASCADE)
    data = models.DateField()
    especialista = models.CharField(max_length=100)  

    def __str__(self):
        return f'{self.usuario.username} - {self.especialidade.nome} em {self.local.nome} na {self.data}'


# Armazena os sintomas relatados por um usuário
class SintomasUsuario(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    sintomas = models.TextField()
    periodo = models.CharField(max_length=100, default='Desconhecido') 
    dor = models.IntegerField(default=0)
    quando_dor = models.CharField(max_length=50, default='Nunca')  
    algo_mais = models.TextField(blank=True, default='N/A')  
    created_at = models.DateTimeField(auto_now_add=True)  # Armazena a data/hora em que o registro foi criado

    def __str__(self):
        return f"Sintomas de {self.usuario.username}"

    @classmethod    
    def get_consultas(cls):
        return cls.objects.all()


# Representa um bairro onde uma UPA está localizada
class Bairros(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome


# Locais específicos de UPAs dentro de um bairro
class Locais(models.Model):
    nome = models.CharField(max_length=100)
    bairro = models.ForeignKey(Bairros, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.nome


# Informações adicionais sobre os locais das UPAs
class Info_local(models.Model):
    nome = models.TextField(blank=True, null=True)
    locais = models.ForeignKey(Locais, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return self.nome

# Representa um bairro onde os postos de saúde estão localizados
class PostosBairro(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome


# Locais específicos dos postos de saúde dentro de um bairro
class Endereco(models.Model):
    nome = models.CharField(max_length=100)
    posto_bairro = models.ForeignKey(PostosBairro, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.nome


# Informações adicionais sobre os locais das UPAs
class Horario(models.Model):
    nome = models.TextField(blank=True, null=True)
    posto_horario = models.ForeignKey(Endereco, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return self.nome