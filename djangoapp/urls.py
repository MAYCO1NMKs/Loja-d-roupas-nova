
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import RedirectView
from django.contrib.staticfiles.urls import staticfiles_urlpatterns # Importação correta

# A view da página inicial é importada do app 'produtos'
from produtos.views import home_view

urlpatterns = [
    # Rotas do Admin
    path('admin/', admin.site.urls),

    # Rotas de Autenticação (django-allauth)
    path('accounts/', include('allauth.urls')),

    # Rotas da API (dj-rest-auth)
    path('api/auth/', include('dj_rest_auth.urls')),
    path('api/auth/registration/', include('dj_rest_auth.registration.urls')),

    # Rotas dos Aplicativos
    path('', home_view, name='home'),
    path('produtos/', include(('produtos.urls', 'produtos'), namespace='produtos')),
    path('usuario/', include(('usuario.urls', 'usuario'), namespace='usuario')),
    path('carrinho/', include(('carrinho.urls', 'carrinho'), namespace='carrinho')),
    path('pedidos/', include('pedidos.urls')),

    # --- Redirecionamentos para Melhor Experiência ---
    path('login/', RedirectView.as_view(url='/accounts/login/', permanent=False)),
    path('accounts/profile/', RedirectView.as_view(url='/usuario/profile/', permanent=True)),
]

# --- Configuração para Servir Arquivos Estáticos e de Mídia em Desenvolvimento ---
if settings.DEBUG:
    # Adiciona as URLs para servir arquivos estáticos (CSS, JS, etc.)
    urlpatterns += staticfiles_urlpatterns()
    # Adiciona as URLs para servir arquivos de mídia (uploads)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

