from django.urls import path
from .views import ProdutoListAPIView

app_name = 'produtos_api'

urlpatterns = [
    path('produtos/', ProdutoListAPIView.as_view(), name='lista_produtos_api'),
]
