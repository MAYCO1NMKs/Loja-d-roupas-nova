from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from produtos.models import Produto
from .models import Carrinho, ItemCarrinho

def _get_carrinho(request):
    """
    Função utilitária para obter ou criar um carrinho associado à sessão atual.
    """
    id_sessao = request.session.session_key
    if not id_sessao:
        request.session.create()
        id_sessao = request.session.session_key
    
    carrinho, criado = Carrinho.objects.get_or_create(id_sessao=id_sessao)
    return carrinho

@require_POST
def adicionar_ao_carrinho(request, produto_id):
    """
    Adiciona um produto ao carrinho ou incrementa sua quantidade se já existir.
    """
    carrinho = _get_carrinho(request)
    produto = get_object_or_404(Produto, id=produto_id)
    
    # Tenta encontrar o item no carrinho
    item, criado = ItemCarrinho.objects.get_or_create(
        carrinho=carrinho,
        produto=produto
    )
    
    # Se o item não foi criado (já existia), incrementa a quantidade
    if not criado:
        item.quantidade += 1
        item.save()
        
    return redirect('carrinho:ver_carrinho')

def ver_carrinho(request):
    """
    Exibe o conteúdo do carrinho de compras.
    """
    carrinho = _get_carrinho(request)
    return render(request, 'carrinho/ver_carrinho.html', {'carrinho': carrinho})
