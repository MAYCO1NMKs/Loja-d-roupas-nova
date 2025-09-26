# pedidos/urls.py
from django.urls import path
from . import views

app_name = 'pedidos'

urlpatterns = [
    path('checkout/', views.checkout, name='checkout'),
    path('criar/', views.criar_pedido, name='criar_pedido'),
    path('sucesso/', views.pedido_sucesso, name='pedido_sucesso'),
]
