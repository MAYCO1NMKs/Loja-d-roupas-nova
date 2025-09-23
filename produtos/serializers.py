from rest_framework import serializers
from .models import Produto, VariacaoProduto

class VariacaoProdutoSerializer(serializers.ModelSerializer):
    class Meta:
        model = VariacaoProduto
        fields = ['tamanho', 'estoque']

class ProdutoSerializer(serializers.ModelSerializer):
    variacoes = VariacaoProdutoSerializer(many=True, read_only=True)

    class Meta:
        model = Produto
        fields = ['id', 'nome', 'slug', 'descricao', 'preco', 'imagem', 'disponivel', 'variacoes']
