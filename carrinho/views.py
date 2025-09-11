from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from produtos.models import Produto
from .models import Carrinho, ItemCarrinho
from django.db.models import F

@login_required
def adicionar_ao_carrinho(request, produto_id):
    """
    View para adicionar um produto ao carrinho do usuário.
    Verifica se o usuário já tem um carrinho. Se não, cria um.
    Verifica se o item já existe no carrinho. Se sim, incrementa a quantidade.
    Se não, cria um novo ItemCarrinho.
    """
    produto = get_object_or_404(Produto, id=produto_id)
    # Garante que o usuário tem um carrinho, criando-o se necessário
    carrinho, criado = Carrinho.objects.get_or_create(usuario=request.user)

    # Verifica se o item já está no carrinho
    try:
        item_carrinho = ItemCarrinho.objects.get(carrinho=carrinho, produto=produto)
        # Se o item existe, incrementa a quantidade usando F() para evitar condições de corrida
        item_carrinho.quantidade = F('quantidade') + 1
        item_carrinho.save(update_fields=['quantidade'])
        
        # Recarrega o objeto do banco de dados para obter o valor atualizado
        item_carrinho.refresh_from_db()

    except ItemCarrinho.DoesNotExist:
        # Se o item não existe, cria um novo
        item_carrinho = ItemCarrinho.objects.create(carrinho=carrinho, produto=produto, quantidade=1)
    
    return redirect('ver_carrinho')

@login_required
def ver_carrinho(request):
    """
    View para exibir o conteúdo do carrinho do usuário.
    Garante que o carrinho existe.
    """
    try:
        carrinho = Carrinho.objects.get(usuario=request.user)
    except Carrinho.DoesNotExist:
        carrinho = None
    
    return render(request, 'carrinho/ver_carrinho.html', {'carrinho': carrinho})
