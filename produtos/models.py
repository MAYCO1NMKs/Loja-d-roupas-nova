
from django.db import models
from django.utils.text import slugify


class Produto(models.Model):
    """Representa um produto na loja, como uma camisa ou calça."""

    nome = models.CharField(max_length=255)
    descricao = models.TextField()
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    imagem = models.ImageField(upload_to="produtos/", blank=True, null=True)
    destaque = models.BooleanField(default=False)
    slug = models.SlugField(max_length=255, unique=True, blank=True)

    class Meta:
        verbose_name = "Produto"
        verbose_name_plural = "Produtos"
        ordering = ("nome",)

    def __str__(self):
        return self.nome

    def save(self, *args, **kwargs):
        """Gera o slug automaticamente a partir do nome do produto se não existir."""
        if not self.slug:
            self.slug = slugify(self.nome)
        super().save(*args, **kwargs)


class VariacaoProduto(models.Model):
    """Representa uma variação de um produto, como tamanho e estoque."""

    TAMANHO_CHOICES = [
        ("P", "Pequeno"),
        ("M", "Médio"),
        ("G", "Grande"),
        ("GG", "Extra Grande"),
    ]

    produto = models.ForeignKey(Produto, related_name="variacoes", on_delete=models.CASCADE)
    tamanho = models.CharField(max_length=2, choices=TAMANHO_CHOICES)
    estoque = models.PositiveIntegerField()

    class Meta:
        verbose_name = "Variação de Produto"
        verbose_name_plural = "Variações de Produtos"
        unique_together = ("produto", "tamanho")

    def __str__(self):
        return f"{self.produto.nome} - {self.get_tamanho_display()}"
