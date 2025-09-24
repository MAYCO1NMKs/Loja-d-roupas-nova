
from django.contrib import admin

from .models import ItemPedido, Pedido


class ItemPedidoInline(admin.TabularInline):
    """Permite a edição dos itens do pedido na página do pedido."""

    model = ItemPedido
    extra = 0
    readonly_fields = ("produto", "quantidade", "preco")
    can_delete = False


@admin.register(Pedido)
class PedidoAdmin(admin.ModelAdmin):
    """Configuração do admin para o modelo de Pedido."""

    list_display = ("id", "usuario", "get_total_pedido", "criado_em", "status")
    list_filter = ("status", "criado_em")
    search_fields = ("id", "usuario__username")
    inlines = [ItemPedidoInline]
    readonly_fields = ("usuario", "criado_em", "atualizado_em")

    def get_total_pedido(self, obj):
        return f"R$ {obj.get_total_pedido:.2f}"

    get_total_pedido.short_description = "Total do Pedido"


@admin.register(ItemPedido)
class ItemPedidoAdmin(admin.ModelAdmin):
    """Configuração do admin para o modelo de ItemPedido."""

    list_display = ("pedido", "produto", "quantidade", "preco", "get_subtotal")
    list_filter = ("pedido__status",)
    search_fields = ("pedido__id", "produto__nome")

    def get_subtotal(self, obj):
        return f"R$ {obj.get_subtotal:.2f}"

    get_subtotal.short_description = "Subtotal"
