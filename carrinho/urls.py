from django.urls import path
from . import views

app_name = 'carrinho'

urlpatterns = [
    path('', views.ver_carrinho, name='ver_carrinho'),
    path('adicionar/<int:produto_id>/', views.adicionar_ao_carrinho, name='adicionar_ao_carrinho'),
    # A nova URL para remover itens foi adicionada aqui.
    path('remover/<int:item_id>/', views.remover_do_carrinho, name='remover_do_carrinho'),
]
