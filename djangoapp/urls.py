from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

# Importa a view da página inicial diretamente do app produtos
from produtos.views import home_view

urlpatterns = [
    path('admin/', admin.site.urls),

    # --- ROTAS DA API ---
    # Centraliza todas as rotas da API sob o prefixo /api/
    path('api/produtos/', include('produtos.urls')), # Rotas de produtos
    path('api/auth/', include('dj_rest_auth.urls')), # Rotas de login, logout, etc.
    path('api/auth/registration/', include('dj_rest_auth.registration.urls')), # Rotas de registro


    # --- Rotas Antigas (Templates) ---
    # Mantemos a home por enquanto, mas as outras serão substituídas pelo front-end
    path('', home_view, name='home'),
    path('usuario/', include(('usuario.urls', 'usuario'), namespace='usuario')),
    path('carrinho/', include(('carrinho.urls', 'carrinho'), namespace='carrinho')),
    path('pedidos/', include('pedidos.urls')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
