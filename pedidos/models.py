from django.db import models
from django.conf import settings
from produtos.models import Produto

# Definimos as opções de status do pedido
STATUS_PEDIDO = (
    ('Pendente', 'Pendente'),
    ('Processando', 'Processando'),
    ('Enviado', 'Enviado'),
    ('Entregue', 'Entregue'),
    ('Cancelado', 'Cancelado'),
)

class Pedido(models.Model):
    """
    Representa um pedido de um usuário.
    """
    usuario = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='pedidos'
    )
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)
    status = models.CharField(
        max_length=50,
        choices=STATUS_PEDIDO,
        default='Pendente'
    )
    
    class Meta:
        verbose_name = "Pedido"
        verbose_name_plural = "Pedidos"
        ordering = ('-criado_em',)

    def __str__(self):
        return f'Pedido {self.id} de {self.usuario.username}'
    
    @property
    def get_total_pedido(self):
        """Calcula o valor total do pedido."""
        return sum(item.get_subtotal for item in self.itens.all())


class ItemPedido(models.Model):
    """
    Representa um item dentro de um pedido.
    """
    pedido = models.ForeignKey(
        Pedido,
        on_delete=models.CASCADE,
        related_name='itens'
    )
    produto = models.ForeignKey(
        Produto,
        on_delete=models.CASCADE,
        related_name='itens_pedido'
    )
    quantidade = models.PositiveIntegerField(default=1)
    preco = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        verbose_name = "Item do Pedido"
        verbose_name_plural = "Itens do Pedido"

    def __str__(self):
        return f'{self.quantidade} x {self.produto.nome}'
    
    @property
    def get_subtotal(self):
        """Calcula o subtotal de um item do pedido."""
        return self.quantidade * self.preco
