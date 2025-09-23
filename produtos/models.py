from django.db import models
from django.urls import reverse

# Modelo para os Produtos
class Produto(models.Model):
    nome = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True, unique=True)
    imagem = models.ImageField(upload_to='products/%Y/%m/%d', blank=True)
    descricao = models.TextField(blank=True)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    # Novo campo para marcar produtos como destaque
    destaque = models.BooleanField(default=False)
    disponivel = models.BooleanField(default=True)
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('nome',)
        # O 'db_table' especifica o nome da tabela no banco de dados.
        db_table = 'produto'
        # O 'verbose_name_plural' é usado no painel de administração do Django.
        verbose_name_plural = 'produtos'

    def __str__(self):
        return self.nome

    def get_absolute_url(self):
        return reverse('produtos:detalhe_produto', args=[self.id, self.slug])

# Modelo para as Variações de Tamanho dos Produtos
class VariacaoProduto(models.Model):
    TAMANHO_CHOICES = (
        ('P', 'Pequeno'),
        ('M', 'Médio'),
        ('G', 'Grande'),
        ('GG', 'Extra Grande'),
    )
    produto = models.ForeignKey(Produto, related_name='variacoes', on_delete=models.CASCADE)
    tamanho = models.CharField(max_length=2, choices=TAMANHO_CHOICES)
    estoque = models.PositiveIntegerField(default=0)

    class Meta:
        # Garante que cada produto só pode ter uma variação de um determinado tamanho
        unique_together = ('produto', 'tamanho')
        db_table = 'variacao_produto'
        verbose_name_plural = 'variações de produto'

    def __str__(self):
        return f'{self.produto.nome} - Tamanho: {self.tamanho} (Estoque: {self.estoque})'
