
from django.contrib import admin

from .models import Produto, VariacaoProduto


class VariacaoProdutoInline(admin.TabularInline):
    """Permite a edição de variações de produto na página do produto."""

    model = VariacaoProduto
    extra = 1


@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    """Configura a interface de administração para o modelo Produto."""

    list_display = ("nome", "preco", "destaque", "slug")
    list_filter = ("destaque",)
    list_editable = ("preco", "destaque")
    prepopulated_fields = {"slug": ("nome",)}
    inlines = [VariacaoProdutoInline]


@admin.register(VariacaoProduto)
class VariacaoProdutoAdmin(admin.ModelAdmin):
    """Configura a interface de administração para o modelo VariacaoProduto."""

    list_display = ("produto", "tamanho", "estoque")
    list_filter = ("tamanho", "produto__nome")
    search_fields = ("produto__nome",)
