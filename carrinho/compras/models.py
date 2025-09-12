
from django.db import models
from produtos.models import Produto

class Carrinho(models.Model):
    id_sessao = models.CharField(max_length=255, blank=True)
    data_criacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.id_sessao

class ItemCarrinho(models.Model):
    carrinho = models.ForeignKey(Carrinho, related_name='itens', null=True, blank=True, on_delete=models.CASCADE)
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    quantidade = models.IntegerField(default=1)
    ativo = models.BooleanField(default=True)

    def subtotal(self):
        return self.produto.preco * self.quantidade

    def __str__(self):
        return self.produto.nome
