from django.db import models
from usuario.models import CustomUser
from produtos.models import Produto

class Carrinho(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    quantidade = models.PositiveIntegerField(default=1)
    adicionado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.quantidade} x {self.produto.nome} ({self.user.username})"
