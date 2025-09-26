# pedidos/models.py
from django.db import models
from django.conf import settings
from produtos.models import VariacaoProduto

class Pedido(models.Model):
    STATUS_CHOICES = (
        ('pendente', 'Pendente'),
        ('processando', 'Processando'),
        ('enviado', 'Enviado'),
        ('entregue', 'Entregue'),
        ('cancelado', 'Cancelado'),
    )
    METODO_PAGAMENTO_CHOICES = (
        ('pix', 'Pix'),
        ('cartao', 'Cartão de Crédito/Débito'),
    )

    # Dados do Pedido
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True)
    id_sessao = models.CharField(max_length=32, null=True, blank=True)
    total = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pendente')
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)
    
    # Dados do Cliente
    nome_cliente = models.CharField(max_length=100)
    email_cliente = models.EmailField()
    telefone_cliente = models.CharField(max_length=20)

    # Dados do Pagamento
    metodo_pagamento = models.CharField(max_length=20, choices=METODO_PAGAMENTO_CHOICES)

    def __str__(self):
        return f"Pedido #{self.id} - {self.status}"

class ItemPedido(models.Model):
    pedido = models.ForeignKey(Pedido, related_name='itens', on_delete=models.CASCADE)
    variacao = models.ForeignKey(VariacaoProduto, on_delete=models.PROTECT)
    quantidade = models.PositiveIntegerField()
    preco = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.quantidade}x {self.variacao.produto.nome} ({self.variacao.get_tamanho_display()})"

    def get_subtotal(self):
        return self.quantidade * self.preco
