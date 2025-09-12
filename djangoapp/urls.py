
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import RedirectView

# Importa a view da página inicial diretamente do app produtos
from produtos.views import home_view

urlpatterns = [
    path('admin/', admin.site.urls),

    # --- CONTORNOS PARA PROBLEMAS DE REDIRECIONAMENTO ---
    # Captura a URL de login incorreta e a redireciona para a correta.
    path('login/', RedirectView.as_view(url='/accounts/login/', permanent=False)),
    # Redireciona a URL de perfil padrão do allauth para a página de perfil personalizada.
    path('accounts/profile/', RedirectView.as_view(url='/usuario/profile/', permanent=True)),


    # --- ROTAS DE AUTENTICAÇÃO (django-allauth) ---
    # Fornecem as páginas de login, logout, registro, etc.
    path('accounts/', include('allauth.urls')),

    # --- ROTAS DA API ---
    # Centraliza todas as rotas da API sob o prefixo /api/
    path('api/auth/', include('dj_rest_auth.urls')), # Rotas de login, logout, etc. para API
    path('api/auth/registration/', include('dj_rest_auth.registration.urls')), # Rotas de registro para API

    # --- Rotas do Site (Templates) ---
    path('', home_view, name='home'),
    path('produtos/', include(('produtos.urls', 'produtos'), namespace='produtos')),
    path('usuario/', include(('usuario.urls', 'usuario'), namespace='usuario')),
    path('carrinho/', include(('carrinho.urls', 'carrinho'), namespace='carrinho')),
    path('pedidos/', include('pedidos.urls')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
