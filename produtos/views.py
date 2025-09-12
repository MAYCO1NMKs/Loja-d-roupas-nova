from django.shortcuts import render
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

# --- Views Antigas (Renderização de HTML) ---

def home_view(request):
    """
    View para a página inicial do site.
    """
    return render(request, 'home.html')

def lista_produtos(request):
    """
    Visualização para exibir a lista de todos os produtos disponíveis.
    """
    produtos = Produto.objects.filter(disponivel=True)
    context = {
        'produtos': produtos
    }
    return render(request, 'produtos/lista_produtos.html', context)
