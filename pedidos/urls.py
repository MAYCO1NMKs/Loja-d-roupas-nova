from django.urls import path
from . import views

urlpatterns = [
    # Rota para finalizar o pedido a partir do carrinho
    path('finalizar/', views.finalizar_pedido, name='finalizar_pedido'),
    
    # Rota para ver o histórico de pedidos do usuário
    path('historico/', views.historico_pedidos, name='historico_pedidos'),
]
