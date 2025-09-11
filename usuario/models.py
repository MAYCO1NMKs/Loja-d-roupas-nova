from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    telefone = models.CharField(max_length=15, blank=True)
    endereco = models.TextField(blank=True)

class Profile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)

    def __str__(self):
        return self.user.username
