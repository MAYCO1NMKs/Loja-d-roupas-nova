from django.urls import path
from . import views

# Define o namespace para este aplicativo
app_name = 'produtos'

urlpatterns = [
    # O caminho agora é '' (vazio), pois o prefixo /produtos/ será definido no arquivo de URLs principal.
    path('', views.lista_produtos, name='lista_produtos'),
]
