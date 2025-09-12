from rest_framework import serializers
from .models import Produto, Categoria

class CategoriaSerializer(serializers.ModelSerializer):
    """
    Serializer para o modelo Categoria.
    """
    class Meta:
        model = Categoria
        fields = ['id', 'nome']

class ProdutoSerializer(serializers.ModelSerializer):
    """
    Serializer para o modelo Produto. Inclui a categoria aninhada.
    """
    categoria = CategoriaSerializer(read_only=True)

    class Meta:
        model = Produto
        fields = ['id', 'nome', 'descricao', 'preco', 'imagem', 'categoria', 'disponivel']
