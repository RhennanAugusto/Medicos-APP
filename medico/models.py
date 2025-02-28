from django.db import models
from django.contrib.auth.models import User
#utilizo essa aba para adicionar dados da minha aplicação que o django não consegue oferecer ja automatizado
#URM é uma forma de escrever codigo usando uma linguagem de programção e o codigo ser convertido no banco

def is_medico(user):
    return DadosMedico.objects.filter(user = user).exists()

class Especialidades(models.Model):
    especialidade = models.CharField(max_length=100)

    def __str__(self):
        return self.especialidade

class DadosMedico(models.Model):
    crm = models.CharField(max_length=30)
    nome = models.CharField(max_length=100)
    cep = models.CharField(max_length=15)
    rua = models.CharField(max_length=100)
    bairro = models.CharField(max_length=100)
    numero = models.IntegerField()
    rg = models.ImageField(upload_to='rgs')
    cedula_identidade_medica = models.ImageField(upload_to='cim')
    foto = models.ImageField(upload_to='fotos_perfil')
    descricao = models.TextField() #TEXT FIELD NÃO TEM LIMITAÇÃO DE CARACTERES
    valor_consulta = models.FloatField(default=100)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    especialidade = models.ForeignKey(Especialidades, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.user.username