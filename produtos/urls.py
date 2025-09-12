from django.urls import path
from .views import lista_produtos, detalhe_produto, ProdutoListAPIView

app_name = 'produtos'

urlpatterns = [
    # Rota para a página web que lista os produtos (e.g., /produtos/)
    path('', lista_produtos, name='lista_produtos'),
    
    # Rota para a página de detalhes de um produto (e.g., /produtos/1/)
    path('<int:produto_id>/', detalhe_produto, name='detalhe_produto'),
    
    # Rota para a API (e.g., /produtos/api/)
    path('api/', ProdutoListAPIView.as_view(), name='lista_produtos_api'),
]
