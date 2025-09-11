from django.shortcuts import render, redirect
from .models import Pedido
from produtos.models import Produto

def carrinho(request):
    produtos = Produto.objects.all()
    return render(request, 'carrinho.html', {'produtos': produtos})
