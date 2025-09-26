
from django.contrib import admin

from .models import ItemPedido, Pedido


class ItemPedidoInline(admin.TabularInline):
    """Permite a edição dos itens do pedido na página do pedido."""

    model = ItemPedido
    extra = 0
    # Corrigido: Acessando o produto através da variação
    readonly_fields = ("variacao", "quantidade", "preco") 
    can_delete = False


@admin.register(Pedido)
class PedidoAdmin(admin.ModelAdmin):
    """Configuração do admin para o modelo de Pedido."""

    list_display = ("id", "usuario", "total", "criado_em", "status")
    list_filter = ("status", "criado_em")
    search_fields = ("id", "usuario__username")
    inlines = [ItemPedidoInline]
    readonly_fields = ("usuario", "criado_em", "atualizado_em")


@admin.register(ItemPedido)
class ItemPedidoAdmin(admin.ModelAdmin):
    """Configuração do admin para o modelo de ItemPedido."""

    # Corrigido: Acessando o nome do produto através da variação
    list_display = ("pedido", "variacao", "quantidade", "preco", "get_subtotal")
    list_filter = ("pedido__status",)
    # Corrigido: Acessando o nome do produto através da variação para a busca
    search_fields = ("pedido__id", "variacao__produto__nome")

