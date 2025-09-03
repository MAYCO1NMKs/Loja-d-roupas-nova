from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Profile, Produto, Carrinho
from .forms import ProfileForm

# ----------------------
# LOGIN / LOGOUT / CADASTRO
# ----------------------

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('dashboard')
        else:
            messages.error(request, 'Usuário ou senha incorretos')
    return render(request, 'usuario/login.html')

def logout_view(request):
    logout(request)
    return redirect('login')

def cadastro_view(request):
    if request.method == 'POST':
        username = request.POST.get('username').strip()
        email = request.POST.get('email').strip()
        password = request.POST.get('password').strip()

        if not username or not email or not password:
            messages.error(request, "Todos os campos são obrigatórios.")
            return render(request, 'usuario/cadastro.html')

        if User.objects.filter(username=username).exists():
            messages.error(request, "Usuário já existe.")
            return render(request, 'usuario/cadastro.html')

        User.objects.create_user(username=username, email=email, password=password)
        messages.success(request, "Cadastro realizado com sucesso! Faça login.")
        return redirect('login')

    return render(request, 'usuario/cadastro.html')

# ----------------------
# DASHBOARD
# ----------------------
@login_required(login_url='login')
def dashboard_view(request):
    return render(request, 'usuario/dashboard.html')

# ----------------------
# PERFIL
# ----------------------
@login_required(login_url='login')
def editar_perfil(request):
    profile, _ = Profile.objects.get_or_create(user=request.user)
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, "Perfil atualizado com sucesso!")
            return redirect('perfil')
    else:
        form = ProfileForm(instance=profile)
    return render(request, 'usuario/perfil.html', {'form': form})

# ----------------------
# PRODUTOS E CONTAS
# ----------------------
@login_required(login_url='login')
def gerenciar_produtos(request):
    produtos = Produto.objects.all()
    return render(request, 'usuario/produtos.html', {'produtos': produtos})

@login_required(login_url='login')
def ver_contas(request):
    usuarios = Profile.objects.all()
    return render(request, 'usuario/ver_contas.html', {'usuarios': usuarios})

# ----------------------
# CARRINHO
# ----------------------
@login_required(login_url='login')
def carrinho(request):
    carrinho, _ = Carrinho.objects.get_or_create(usuario=request.user)
    return render(request, 'usuario/carrinho.html', {'carrinho': carrinho})

@login_required(login_url='login')
def adicionar_ao_carrinho(request, produto_id):
    produto = Produto.objects.get(id=produto_id)
    carrinho, _ = Carrinho.objects.get_or_create(usuario=request.user)
    carrinho.produtos.add(produto)
    return redirect('carrinho')

# ----------------------
# PÁGINAS EXTRAS
# ----------------------
def home_view(request):
    contexto = {
        'titulo': 'Página inicial',
        'mensagem': 'Bem-vindo ao site da nossa loja!'
    }
    return render(request, 'usuario/home.html', contexto)

def sobre(request):
    contexto = {
        'titulo': 'Sobre nós',
        'descricao': 'Somos uma loja especializada em roupas de marca.'
    }
    return render(request, 'usuario/home.html', contexto)
