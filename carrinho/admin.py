
from django.contrib import admin

from .models import Carrinho, ItemCarrinho


class ItemCarrinhoInline(admin.TabularInline):
    """Permite a visualização dos itens do carrinho na página do carrinho."""

    model = ItemCarrinho
    extra = 0
    readonly_fields = ("variacao", "quantidade")
    can_delete = False


@admin.register(Carrinho)
class CarrinhoAdmin(admin.ModelAdmin):
    """Configuração do admin para o modelo de Carrinho."""

    list_display = ("id_sessao", "criado_em", "get_total_carrinho", "get_contagem_itens")
    inlines = [ItemCarrinhoInline]
    readonly_fields = ("id_sessao", "criado_em", "atualizado_em")


@admin.register(ItemCarrinho)
class ItemCarrinhoAdmin(admin.ModelAdmin):
    """Configuração do admin para o modelo de ItemCarrinho."""

    list_display = ("carrinho", "variacao", "quantidade", "get_subtotal")
    readonly_fields = ("carrinho", "variacao", "quantidade")
