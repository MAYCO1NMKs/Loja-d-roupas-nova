from django.db import models
from django.conf import settings
from produtos.models import Produto

class Carrinho(models.Model):
    """
    Modelo para o carrinho de compras.
    Cada usuário terá um carrinho associado.
    """
    # A Foreign Key para o modelo de usuário personalizado
    usuario = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='carrinho')
    
    # Campo para armazenar a data de criação do carrinho
    data_criacao = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Carrinho de {self.usuario.username}"

class ItemCarrinho(models.Model):
    """
    Modelo para os itens dentro do carrinho.
    Cada item está associado a um produto e a um carrinho.
    """
    # Foreign Key para o carrinho ao qual o item pertence
    carrinho = models.ForeignKey(Carrinho, on_delete=models.CASCADE, related_name='itens')
    
    # Foreign Key para o produto que o item representa
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    
    # Quantidade do produto no carrinho
    quantidade = models.PositiveIntegerField(default=1)
    
    def __str__(self):
        return f"{self.quantidade}x {self.produto.nome} no carrinho de {self.carrinho.usuario.username}"
