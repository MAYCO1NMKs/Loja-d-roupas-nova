from django.shortcuts import render, get_object_or_404

from .models import Produto


def home_view(request):
    """
    Exibe a página inicial com produtos em destaque que têm estoque.
    """
    # Filtra produtos em destaque com estoque, limitado a 4.
    produtos_destaque = Produto.objects.filter(
        destaque=True, variacoes__estoque__gt=0
    ).distinct()[:4]
    context = {"produtos": produtos_destaque}
    return render(request, "home.html", context)


def colecoes_view(request):
    """
    Exibe a página de coleções com todos os produtos que têm estoque.
    """
    # Filtra todos os produtos com estoque.
    produtos_com_estoque = Produto.objects.filter(
        variacoes__estoque__gt=0
    ).distinct()
    context = {"produtos": produtos_com_estoque}
    return render(request, "produtos/colecoes.html", context)


def detalhe_produto(request, id, slug):
    """
    Exibe os detalhes de um produto específico.
    """
    produto = get_object_or_404(Produto, id=id, slug=slug)
    context = {"produto": produto}
    return render(request, "produtos/detalhe_produto.html", context)
