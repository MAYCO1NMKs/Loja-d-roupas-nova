from django.shortcuts import render, get_object_or_404
from .models import Produto

# Imports para a API
from rest_framework import generics
from .serializers import ProdutoSerializer

# --- Views da API ---

class ProdutoListAPIView(generics.ListAPIView):
    """
    View da API para listar todos os produtos disponíveis.
    """
    queryset = Produto.objects.filter(disponivel=True)
    serializer_class = ProdutoSerializer

# --- Views do Site (Renderização de HTML) ---

def home_view(request):
    """
    View para a página inicial do site.
    Exibe os produtos marcados como disponíveis.
    """
    produtos = Produto.objects.filter(disponivel=True)
    context = {
        'produtos': produtos
    }
    return render(request, 'home.html', context)

def lista_produtos(request):
    """
    View para exibir a lista de todos os produtos disponíveis.
    """
    produtos = Produto.objects.filter(disponivel=True)
    context = {
        'produtos': produtos
    }
    return render(request, 'produtos/lista_produtos.html', context)

def detalhe_produto(request, produto_id):
    """
    View para exibir os detalhes de um único produto.
    """
    produto = get_object_or_404(Produto, id=produto_id, disponivel=True)
    context = {
        'produto': produto
    }
    return render(request, 'produtos/detalhe_produto.html', context)
