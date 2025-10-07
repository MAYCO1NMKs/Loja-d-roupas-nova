from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    """Modelo de usuário personalizado."""

    # Informações de contato e pessoais
    foto_perfil = models.ImageField(upload_to='perfil_pics/', null=True, blank=True)
    telefone = models.CharField(max_length=20, blank=True, null=True)
    data_nascimento = models.DateField(blank=True, null=True)

    # Endereço
    cep = models.CharField(max_length=20, blank=True, null=True)
    estado = models.CharField(max_length=100, blank=True, null=True)
    cidade = models.CharField(max_length=100, blank=True, null=True)
    bairro = models.CharField(max_length=100, blank=True, null=True)
    endereco = models.CharField("Endereço", max_length=255, blank=True, null=True)
    numero = models.CharField("Número", max_length=20, blank=True, null=True)
    complemento = models.CharField(max_length=100, blank=True, null=True)


    def __str__(self):
        return self.username
