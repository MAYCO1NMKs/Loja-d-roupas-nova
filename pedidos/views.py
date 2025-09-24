
from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.shortcuts import get_object_or_404, redirect, render

from carrinho.views import get_carrinho

from .forms import FormularioPedido
from .models import ItemPedido, Pedido


@login_required
def checkout(request):
    """Processa o checkout, coletando os dados do cliente e criando o pedido."""
    carrinho = get_carrinho(request)
    if not carrinho.itens.exists():
        return redirect("carrinho:ver_carrinho")

    if request.method == "POST":
        form = FormularioPedido(request.POST)
        if form.is_valid():
            try:
                with transaction.atomic():
                    pedido = Pedido.objects.create(usuario=request.user)

                    itens_pedido = []
                    for item in carrinho.itens.all():
                        itens_pedido.append(
                            ItemPedido(
                                pedido=pedido,
                                produto=item.produto,
                                preco=item.produto.preco,
                                quantidade=item.quantidade,
                            )
                        )

                    ItemPedido.objects.bulk_create(itens_pedido)
                    carrinho.itens.all().delete()

                    return redirect("pedidos:pedido_confirmado", pedido_id=pedido.id)

            except Exception as e:
                # Adicionar lógica para lidar com o erro, como logging
                print(f"Erro no checkout: {e}")
                # Considerar adicionar uma mensagem de erro para o usuário
                return redirect("carrinho:ver_carrinho")
    else:
        form = FormularioPedido()

    context = {"carrinho": carrinho, "form": form}
    return render(request, "pedidos/checkout.html", context)


@login_required
def pedido_confirmado(request, pedido_id):
    """Mostra a página de confirmação de que um pedido foi realizado com sucesso."""
    pedido = get_object_or_404(Pedido, id=pedido_id, usuario=request.user)
    context = {"pedido": pedido}
    return render(request, "pedidos/pedido_confirmado.html", context)


@login_required
def historico_pedidos(request):
    """Exibe o histórico de pedidos do usuário logado."""
    pedidos = Pedido.objects.filter(usuario=request.user).order_by("-criado_em")
    context = {"pedidos": pedidos}
    return render(request, "pedidos/historico_pedidos.html", context)
