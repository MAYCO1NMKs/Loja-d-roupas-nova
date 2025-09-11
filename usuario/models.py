from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    foto_perfil = models.ImageField(upload_to='fotos_perfil/', blank=True, null=True)
