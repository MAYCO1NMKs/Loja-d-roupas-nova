from django.contrib import admin
from .models import Carrinho, ItemCarrinho

class ItemCarrinhoInline(admin.TabularInline):
    """
    Permite a visualização e edição dos itens de um carrinho
    diretamente na página de administração do Carrinho.
    """
    model = ItemCarrinho
    extra = 0 # Não exibe campos vazios por padrão

@admin.register(Carrinho)
class CarrinhoAdmin(admin.ModelAdmin):
    """
    Configura a exibição do modelo Carrinho no painel de administração.
    """
    list_display = ('usuario', 'data_criacao')
    search_fields = ('usuario__username',)
    inlines = [ItemCarrinhoInline]
    
# Não é necessário registrar o ItemCarrinho separadamente,
# pois ele já é gerenciado pelo CarrinhoAdmin com o inline.
