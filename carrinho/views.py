from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from produtos.models import Produto
from .models import Carrinho, ItemCarrinho
from django.db.models import F

@login_required
def adicionar_ao_carrinho(request, produto_id):
    """
    View para adicionar um produto ao carrinho do usuário.
    """
    produto = get_object_or_404(Produto, id=produto_id)
    carrinho, criado = Carrinho.objects.get_or_create(usuario=request.user)

    try:
        item_carrinho = ItemCarrinho.objects.get(carrinho=carrinho, produto=produto)
        item_carrinho.quantidade = F('quantidade') + 1
        item_carrinho.save(update_fields=['quantidade'])
    except ItemCarrinho.DoesNotExist:
        item_carrinho = ItemCarrinho.objects.create(carrinho=carrinho, produto=produto, quantidade=1)
    
    return redirect('carrinho:ver_carrinho')

@login_required
def ver_carrinho(request):
    """
    View para exibir o conteúdo do carrinho do usuário.
    """
    try:
        carrinho = Carrinho.objects.get(usuario=request.user)
    except Carrinho.DoesNotExist:
        carrinho = None
    
    return render(request, 'carrinho/ver_carrinho.html', {'carrinho': carrinho})

@require_POST
@login_required
def remover_do_carrinho(request, item_id):
    """
    View para remover um item específico do carrinho do usuário.
    """
    item_carrinho = get_object_or_404(ItemCarrinho, id=item_id, carrinho__usuario=request.user)
    item_carrinho.delete()
    
    return redirect('carrinho:ver_carrinho')
