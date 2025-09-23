from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.db import transaction
from .models import Pedido, ItemPedido
from carrinho.views import get_carrinho
from .forms import FormularioPedido

@login_required
def checkout(request):
    """
    Processa o checkout, coletando os dados do cliente e criando o pedido.
    """
    carrinho = get_carrinho(request)
    if not carrinho.itens.exists():
        # Redireciona para o carrinho se ele estiver vazio
        return redirect('carrinho:ver_carrinho')

    if request.method == 'POST':
        form = FormularioPedido(request.POST)
        if form.is_valid():
            try:
                with transaction.atomic():
                    # Cria o objeto Pedido, mas não salva no banco ainda
                    pedido = Pedido(usuario=request.user)

                    # Você pode usar os dados do formulário aqui se precisar
                    # Por exemplo: salvar o endereço no pedido
                    # pedido.endereco_entrega = form.cleaned_data['endereco_linha_1']
                    # ... (isso exigiria adicionar campos ao modelo Pedido)

                    pedido.save() # Salva o pedido para obter um ID

                    # Itera sobre os itens do carrinho e cria os Itens do Pedido
                    for item in carrinho.itens.all():
                        ItemPedido.objects.create(
                            pedido=pedido,
                            produto=item.produto,
                            preco=item.produto.preco,
                            quantidade=item.quantidade
                        )

                    # Limpa o carrinho
                    carrinho.itens.all().delete()

                    # Redireciona para a página de confirmação do pedido
                    return redirect('pedidos:pedido_confirmado', pedido_id=pedido.id)
            except Exception as e:
                # Em caso de erro, a transação é desfeita.
                # Aqui você pode adicionar uma mensagem de erro para o usuário.
                print(f"Erro no checkout: {e}")
                # Futuramente, podemos adicionar uma mensagem de erro no template.
                return redirect('carrinho:ver_carrinho')
    else:
        # Se não for POST, apenas cria um formulário em branco
        form = FormularioPedido()

    return render(request, 'pedidos/checkout.html', {'carrinho': carrinho, 'form': form})


@login_required
def pedido_confirmado(request, pedido_id):
    """
    Mostra a página de confirmação de que um pedido foi realizado com sucesso.
    """
    pedido = get_object_or_404(Pedido, id=pedido_id, usuario=request.user)
    return render(request, 'pedidos/pedido_confirmado.html', {'pedido': pedido})


@login_required
def historico_pedidos(request):
    """
    Exibe o histórico de pedidos do usuário logado.
    """
    pedidos = Pedido.objects.filter(usuario=request.user).order_by('-criado_em')
    return render(request, 'pedidos/historico_pedidos.html', {'pedidos': pedidos})
