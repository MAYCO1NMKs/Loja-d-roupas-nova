
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import RedirectView
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

# Importa a view diretamente para a rota final
from produtos.views import home_view
from usuario.views import profile_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('api/auth/', include('dj_rest_auth.urls')),
    path('api/auth/registration/', include('dj_rest_auth.registration.urls')),
    path('', home_view, name='home'),
    path('produtos/', include(('produtos.urls', 'produtos'), namespace='produtos')),
    path('usuario/', include(('usuario.urls', 'usuario'), namespace='usuario')),
    path('carrinho/', include(('carrinho.urls', 'carrinho'), namespace='carrinho')),
    path('pedidos/', include('pedidos.urls')),

    # --- Redirecionamentos e Rotas de Compatibilidade ---
    path('login/', RedirectView.as_view(url='/accounts/login/', permanent=False)),
    
    # Redireciona o /accounts/profile/ do allauth para o perfil correto.
    path('accounts/profile/', RedirectView.as_view(url='/usuario/perfil/', permanent=True)),
    
    # ROTA FINAL: Aponta a URL antiga diretamente para a view correta.
    # Isso resolve o problema de cache de forma definitiva.
    path('usuario/profile/', profile_view, name='profile_legacy_direct'),
]

if settings.DEBUG:
    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
