from django.shortcuts import render, get_object_or_404
from rest_framework import viewsets
from .models import Produto
from .serializers import ProdutoSerializer

# View para a página inicial, que lista os produtos em destaque
def home_view(request):
    produtos = Produto.objects.filter(disponivel=True, destaque=True)
    return render(request, 'home.html', {'produtos': produtos})

# NOVA VIEW: para a página de coleções, que lista apenas produtos EM DESTAQUE
def colecoes_view(request):
    produtos_destaque = Produto.objects.filter(disponivel=True, destaque=True)
    return render(request, 'produtos/lista_produtos.html', {'produtos': produtos_destaque})

# View para a página de detalhes de um único produto
def detalhe_produto(request, id, slug):
    produto = get_object_or_404(Produto, id=id, slug=slug, disponivel=True)
    # As variações de tamanho estarão disponíveis no template através de `produto.variacoes.all`
    return render(request, 'produtos/detalhe_produto.html', {'produto': produto})

# ViewSet para a API REST (útil para o futuro)
class ProdutoViewSet(viewsets.ModelViewSet):
    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializer
