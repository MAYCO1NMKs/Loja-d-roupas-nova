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

class Cor(models.Model):
    """
    Representa uma cor de produto. Ex: Preto, Branco, Azul.
    """
    nome = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.nome

class Tamanho(models.Model):
    """
    Representa um tamanho de produto. Ex: P, M, G, GG.
    """
    nome = models.CharField(max_length=5, unique=True)

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
    categoria = models.ForeignKey(Categoria, on_delete=models.SET_NULL, null=True, blank=True, related_name='produtos')
    cores = models.ManyToManyField(Cor, blank=True, related_name='produtos')
    tamanhos = models.ManyToManyField(Tamanho, blank=True, related_name='produtos')
    data_criacao = models.DateTimeField(auto_now_add=True)
    disponivel = models.BooleanField(default=True)

    class Meta:
        ordering = ['-data_criacao']

    def __str__(self):
        return self.nome
