from django.db import models
from django.conf import settings
from produtos.models import Produto

class Pedido(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    produtos = models.ManyToManyField(Produto)
    total = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    data = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Pedido {self.id} de {self.user.username}"
