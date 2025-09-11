from django.db import models

class Categoria(models.Model):
    """
    Representa uma categoria de produto.
    """
    nome = models.CharField(max_length=100, unique=True)

    class Meta:
        verbose_name_plural = 'Categorias'

    def __str__(self):
        return self.nome

class Produto(models.Model):
    """
    Representa um produto na loja.
    """
    nome = models.CharField(max_length=200)
    descricao = models.TextField()
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    imagem = models.ImageField(upload_to='produtos/', blank=True, null=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.SET_NULL, null=True, related_name='produtos')
    data_criacao = models.DateTimeField(auto_now_add=True)
    disponivel = models.BooleanField(default=True)

    class Meta:
        ordering = ['-data_criacao']

    def __str__(self):
        return self.nome
