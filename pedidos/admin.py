from django.contrib import admin
from .models import Pedido, ItemPedido

class ItemPedidoInline(admin.TabularInline):
    """
    Permite a edição dos itens do pedido diretamente na página do pedido no painel admin.
    """
    model = ItemPedido
    extra = 0
    readonly_fields = ['produto', 'quantidade', 'preco']
    can_delete = False

class PedidoAdmin(admin.ModelAdmin):
    """
    Configuração do painel admin para o modelo de Pedido.
    """
    list_display = ['id', 'usuario', 'get_total_pedido', 'criado_em', 'status']
    list_filter = ['status', 'criado_em']
    search_fields = ['id', 'usuario__username']
    inlines = [ItemPedidoInline]
    readonly_fields = ['usuario', 'criado_em', 'atualizado_em']

    def get_total_pedido(self, obj):
        return f"R$ {obj.get_total_pedido():.2f}"
    get_total_pedido.short_description = "Total do Pedido"
    
# Registra os modelos no painel de administração
admin.site.register(Pedido, PedidoAdmin)
admin.site.register(ItemPedido)
