from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    # Incluindo as URLs dos seus aplicativos
    path('', include('produtos.urls')),  # Para a página inicial com a lista de produtos
    path('usuario/', include('usuario.urls')),
    path('carrinho/', include('carrinho.urls')),
    path('pedidos/', include('pedidos.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)