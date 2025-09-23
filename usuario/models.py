from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    # Campo existente
    foto_perfil = models.ImageField(upload_to='fotos_perfil/', blank=True, null=True)

    # Novos campos para contato e endereço
    telefone = models.CharField(max_length=20, blank=True, null=True, help_text='(XX) XXXXX-XXXX')
    cep = models.CharField('CEP', max_length=10, blank=True, null=True)
    endereco = models.CharField('Endereço', max_length=255, blank=True, null=True)
    numero = models.CharField('Número', max_length=20, blank=True, null=True)
    complemento = models.CharField(max_length=100, blank=True, null=True)
    bairro = models.CharField(max_length=100, blank=True, null=True)
    cidade = models.CharField(max_length=100, blank=True, null=True)
    estado = models.CharField('UF', max_length=2, blank=True, null=True)

    def __str__(self):
        return self.username
