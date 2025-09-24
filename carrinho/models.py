
from django.db import models

from produtos.models import VariacaoProduto


class Carrinho(models.Model):
    """Representa o carrinho de compras, associado a uma sessão."""

    id_sessao = models.CharField(max_length=40, db_index=True, unique=True)
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Carrinho"
        verbose_name_plural = "Carrinhos"
        ordering = ("-criado_em",)

    def __str__(self):
        return self.id_sessao

    @property
    def get_total_carrinho(self):
        """Calcula o valor total de todos os itens no carrinho."""
        return sum(item.get_subtotal for item in self.itens.all())

    @property
    def get_contagem_itens(self):
        """Retorna o número total de itens no carrinho."""
        return sum(item.quantidade for item in self.itens.all())


class ItemCarrinho(models.Model):
    """Representa um item específico (variação de produto e quantidade) no carrinho."""

    carrinho = models.ForeignKey(
        Carrinho, related_name="itens", on_delete=models.CASCADE
    )
    variacao = models.ForeignKey(VariacaoProduto, on_delete=models.CASCADE)
    quantidade = models.PositiveIntegerField(default=1)

    class Meta:
        verbose_name = "Item do Carrinho"
        verbose_name_plural = "Itens do Carrinho"
        unique_together = ("carrinho", "variacao")

    def __str__(self):
        return f"{self.quantidade} x {self.variacao.produto.nome} ({self.variacao.get_tamanho_display()})"

    @property
    def get_subtotal(self):
        """Calcula o subtotal para este item (preço * quantidade)."""
        return self.variacao.produto.preco * self.quantidade
