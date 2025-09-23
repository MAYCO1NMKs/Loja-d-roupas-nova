from django.urls import path
from . import views

app_name = 'pedidos'

urlpatterns = [
    # Nova rota para a página de checkout
    path('checkout/', views.checkout, name='checkout'),
    
    # Rota para a página de confirmação do pedido
    path('pedido_confirmado/<int:pedido_id>/', views.pedido_confirmado, name='pedido_confirmado'),
    
    # Rota para ver o histórico de pedidos do usuário
    path('historico/', views.historico_pedidos, name='historico_pedidos'),
]
