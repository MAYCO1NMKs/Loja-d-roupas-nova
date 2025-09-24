
from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.http import require_POST

from produtos.models import Produto, VariacaoProduto

from .models import Carrinho, ItemCarrinho


def get_carrinho(request):
    """Obtém o carrinho da sessão atual ou cria um novo."""
    session_id = request.session.session_key
    if not session_id:
        request.session.create()
        session_id = request.session.session_key

    carrinho, _ = Carrinho.objects.get_or_create(id_sessao=session_id)
    return carrinho


@require_POST
def adicionar_ao_carrinho(request, produto_id):
    """Adiciona ou atualiza uma variação de produto no carrinho."""
    carrinho = get_carrinho(request)
    variacao_id = request.POST.get("variacao_id")
    produto = get_object_or_404(Produto, id=produto_id)

    if not variacao_id:
        messages.error(
            request, "A variação do produto (tamanho) não foi especificada."
        )
        return redirect("produtos:detalhe_produto", id=produto_id, slug=produto.slug)

    variacao = get_object_or_404(VariacaoProduto, id=variacao_id)

    if variacao.produto.id != produto_id:
        messages.error(
            request, "Ocorreu um erro de inconsistência de dados. Tente novamente."
        )
        return redirect("produtos:lista_colecoes")

    item, criado = ItemCarrinho.objects.get_or_create(
        carrinho=carrinho, variacao=variacao
    )

    try:
        quantidade = int(request.POST.get("quantidade", "1"))
    except (ValueError, TypeError):
        quantidade = 1

    override = request.POST.get("override") == "True"
    nova_quantidade = quantidade if criado or override else item.quantidade + quantidade

    if nova_quantidade > variacao.estoque:
        messages.warning(
            request,
            f"Estoque insuficiente. Apenas {variacao.estoque} unidades de "
            f'{variacao.produto.nome} ({variacao.get_tamanho_display()}) foram adicionadas.'
        )
        nova_quantidade = variacao.estoque

    if nova_quantidade <= 0:
        item.delete()
        messages.success(
            request,
            f'"{variacao.produto.nome} ({variacao.get_tamanho_display()})" foi removido do carrinho.'
        )
    else:
        item.quantidade = nova_quantidade
        item.save()
        if criado:
            messages.success(
                request,
                f'"{variacao.produto.nome} ({variacao.get_tamanho_display()})" foi adicionado ao carrinho.'
            )
        else:
            messages.success(
                request,
                f'A quantidade de "{variacao.produto.nome} ({variacao.get_tamanho_display()})" foi atualizada.'
            )

    return redirect("carrinho:ver_carrinho")


def remover_do_carrinho(request, item_id):
    """Remove um item específico do carrinho."""
    carrinho = get_carrinho(request)
    item_carrinho = get_object_or_404(ItemCarrinho, id=item_id, carrinho=carrinho)

    nome_produto = item_carrinho.variacao.produto.nome
    tamanho_produto = item_carrinho.variacao.get_tamanho_display()

    item_carrinho.delete()

    messages.success(request, f'"{nome_produto} ({tamanho_produto})" foi removido do carrinho.')

    return redirect("carrinho:ver_carrinho")


def ver_carrinho(request):
    """Exibe o conteúdo do carrinho de compras."""
    carrinho = get_carrinho(request)
    context = {"carrinho": carrinho}
    return render(request, "carrinho/ver_carrinho.html", context)
