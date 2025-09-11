from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

# Importa a view da página inicial diretamente do app produtos
from produtos.views import home_view

urlpatterns = [
    path('admin/', admin.site.urls),

    # 1. A rota da página inicial agora é tratada no nível do projeto.
    path('', home_view, name='home'),

    # 2. Cada aplicativo é incluído sob seu próprio prefixo e com um namespace.
    # Isso resolve o erro 'NoReverseMatch' de uma vez por todas.
    path('produtos/', include(('produtos.urls', 'produtos'), namespace='produtos')),
    path('usuario/', include(('usuario.urls', 'usuario'), namespace='usuario')),
    path('carrinho/', include(('carrinho.urls', 'carrinho'), namespace='carrinho')),
    path('pedidos/', include('pedidos.urls')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
