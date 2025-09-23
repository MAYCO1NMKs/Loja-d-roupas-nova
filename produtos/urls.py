from django.urls import path
# Importando a nova view de coleções
from .views import home_view, detalhe_produto, colecoes_view

app_name = 'produtos'

urlpatterns = [
    # A URL da lista de produtos (página inicial) é gerenciada no urls.py principal.
    
    # Nova URL para a página de coleções em destaque
    path('colecoes/', colecoes_view, name='lista_colecoes'),
    
    # Esta URL é para a página de detalhes de um produto específico.
    path('<int:id>/<slug:slug>/', detalhe_produto, name='detalhe_produto'),
]
