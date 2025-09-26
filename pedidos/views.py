# pedidos/views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from carrinho.views import get_carrinho
from .models import Pedido, ItemPedido
from .forms import CheckoutForm # Importa o novo formulário

def checkout(request):
    """Exibe a página de checkout com o formulário de dados do cliente."""
    carrinho = get_carrinho(request)
    
    if not carrinho.itens.exists():
        return redirect('carrinho:ver_carrinho')

    # Preenche o formulário com dados do usuário, se estiver logado
    initial_data = {}
    if request.user.is_authenticated:
        initial_data = {
            'nome_cliente': request.user.get_full_name() or request.user.username,
            'email_cliente': request.user.email,
        }

    form = CheckoutForm(initial=initial_data)

    contexto = {
        'carrinho': carrinho,
        'form': form,
    }
    return render(request, 'pedidos/checkout.html', contexto)


def criar_pedido(request):
    """Cria um pedido a partir do carrinho e dos dados do formulário de checkout."""
    if request.method != 'POST':
        return redirect('pedidos:checkout')

    carrinho = get_carrinho(request)
    if not carrinho.itens.exists():
        return redirect('carrinho:ver_carrinho')

    form = CheckoutForm(request.POST)

    if form.is_valid():
        # Se o formulário é válido, cria o pedido mas não salva ainda (commit=False)
        pedido = form.save(commit=False)
        pedido.total = carrinho.get_total_price()

        # Associa o usuário ou a sessão ao pedido
        if request.user.is_authenticated:
            pedido.usuario = request.user
        else:
            pedido.id_sessao = request.session.session_key
        
        # Agora salva o pedido no banco de dados
        pedido.save()

        # Cria os Itens do Pedido
        for item_carrinho in carrinho.itens.all():
            ItemPedido.objects.create(
                pedido=pedido,
                variacao=item_carrinho.variacao,
                quantidade=item_carrinho.quantidade,
                preco=item_carrinho.variacao.produto.get_preco_promocional() # Preço no momento da compra
            )

        # Guarda o ID do pedido na sessão para a página de sucesso
        request.session['id_pedido'] = pedido.id

        # Limpa o carrinho
        carrinho.delete()

        # Redireciona para a página de sucesso
        return redirect(reverse('pedidos:pedido_sucesso'))
    else:
        # Se o formulário for inválido, re-renderiza a página de checkout com os erros
        contexto = {
            'carrinho': carrinho,
            'form': form,
        }
        return render(request, 'pedidos/checkout.html', contexto)


def pedido_sucesso(request):
    """Exibe a página de confirmação de pedido bem-sucedido."""
    id_pedido = request.session.get('id_pedido')
    if not id_pedido:
        return redirect('home')
    
    pedido = get_object_or_404(Pedido, id=id_pedido)

    # Medida de segurança para garantir que o cliente só veja seu próprio pedido
    is_owner = (pedido.usuario and pedido.usuario == request.user) or \
               (pedido.id_sessao and pedido.id_sessao == request.session.session_key)

    if not is_owner:
        return redirect('home')

    # Limpa o id_pedido da sessão após o uso
    if 'id_pedido' in request.session:
        del request.session['id_pedido']
        
    contexto = {
        'pedido': pedido
    }
    return render(request, 'pedidos/pedido_sucesso.html', contexto)
