def sobre(request):
    contexto = {
        'titulo': 'Sobre nós',
        'descricao': 'Somos uma loja especializada em roupas de marca.'
    }
    return render(request, 'usuario/home.html', contexto)