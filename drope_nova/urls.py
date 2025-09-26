# drope_nova/urls.py
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from produtos.views import home_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('contas/', include('django.contrib.auth.urls')),
    path('', home_view, name='home'),
    path('produtos/', include('produtos.urls', namespace='produtos')),
    path('carrinho/', include('carrinho.urls', namespace='carrinho')),
    # Incluindo as URLs do novo aplicativo de pedidos
    path('pedidos/', include('pedidos.urls', namespace='pedidos')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
