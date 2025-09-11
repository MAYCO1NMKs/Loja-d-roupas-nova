from django.urls import path
from . import views

urlpatterns = [
    # Mapeia a URL 'adicionar_ao_carrinho' para a view correspondente
    path('adicionar/<int:produto_id>/', views.adicionar_ao_carrinho, name='adicionar_ao_carrinho'),
    
    # Mapeia a URL 'ver_carrinho' para a view correspondente
    path('', views.ver_carrinho, name='ver_carrinho'),
]
