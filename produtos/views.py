from django.shortcuts import render
from .models import Produto

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
