from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Pedido, ItemPedido
from carrinho.models import Carrinho, ItemCarrinho
from django.db import transaction

@login_required
def finalizar_pedido(request):
    """
    Processa a finalização do pedido, convertendo o carrinho em um pedido.
    """
    # Usamos uma transação para garantir que a operação seja atômica
    # Ou o pedido e os itens são criados e o carrinho é limpo,
    # ou nada é alterado se algo der errado.
    try:
        with transaction.atomic():
            # Obtém o carrinho do usuário logado
            carrinho, criado = Carrinho.objects.get_or_create(usuario=request.user)

            if not carrinho.itens.exists():
                return redirect('ver_carrinho')

            # Cria um novo objeto de Pedido para o usuário
            pedido = Pedido.objects.create(usuario=request.user)
            
            # Move cada item do carrinho para o novo pedido
            for item_carrinho in carrinho.itens.all():
                ItemPedido.objects.create(
                    pedido=pedido,
                    produto=item_carrinho.produto,
                    quantidade=item_carrinho.quantidade,
                    preco=item_carrinho.produto.preco
                )
            
            # Limpa o carrinho do usuário após a criação do pedido
            carrinho.itens.all().delete()
            
            return redirect('historico_pedidos')

    except Exception as e:
        # Em caso de erro, a transação será revertida
        print(f"Erro ao finalizar o pedido: {e}")
        return redirect('ver_carrinho')

@login_required
def historico_pedidos(request):
    """
    Exibe o histórico de pedidos do usuário logado.
    """
    # Obtém todos os pedidos do usuário logado, ordenados do mais recente para o mais antigo
    pedidos = Pedido.objects.filter(usuario=request.user).order_by('-criado_em')
    return render(request, 'pedidos/historico_pedidos.html', {'pedidos': pedidos})
