
from django.shortcuts import render, redirect, get_object_or_404
from produtos.models import Produto
from .models import Carrinho, ItemCarrinho

def _carrinho_id(request):
    """
    Função privada para obter ou criar o ID do carrinho na sessão.
    """
    if not request.session.session_key:
        request.session.create()
    return request.session.session_key

def adicionar_ao_carrinho(request, produto_id):
    """
    Adiciona um produto ao carrinho de compras.
    """
    produto = get_object_or_404(Produto, id=produto_id)
    id_carrinho = _carrinho_id(request)
    carrinho, criado = Carrinho.objects.get_or_create(id_sessao=id_carrinho)

    try:
        item_carrinho = ItemCarrinho.objects.get(produto=produto, carrinho=carrinho)
        item_carrinho.quantidade += 1
        item_carrinho.save()
    except ItemCarrinho.DoesNotExist:
        item_carrinho = ItemCarrinho.objects.create(
            produto=produto,
            quantidade=1,
            carrinho=carrinho
        )
        item_carrinho.save()

    return redirect('compras:ver_carrinho')

def remover_do_carrinho(request, item_id):
    """
    Remove um item específico do carrinho.
    """
    item_carrinho = get_object_or_404(ItemCarrinho, id=item_id)
    item_carrinho.delete()
    return redirect('compras:ver_carrinho')

def ver_carrinho(request):
    """
    Exibe os itens no carrinho de compras.
    """
    total = 0
    contador = 0
    itens_carrinho = []

    try:
        id_carrinho = _carrinho_id(request)
        carrinho = Carrinho.objects.get(id_sessao=id_carrinho)
        itens_carrinho = ItemCarrinho.objects.filter(carrinho=carrinho, ativo=True)
        for item in itens_carrinho:
            total += (item.produto.preco * item.quantidade)
            contador += item.quantidade
    except Carrinho.DoesNotExist:
        pass # Carrinho ainda não existe, não faz nada

    return render(request, 'compras/carrinho.html', {
        'itens_carrinho': itens_carrinho,
        'total': total,
        'contador': contador
    })
