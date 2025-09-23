from django.contrib import admin
from .models import Produto, VariacaoProduto

# Inline para facilitar a adição de variações de produto diretamente na página do produto
class VariacaoProdutoInline(admin.TabularInline):
    model = VariacaoProduto
    extra = 1 # Mostra 1 formulário extra por padrão

@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'preco', 'disponivel', 'criado_em', 'atualizado_em')
    list_filter = ('disponivel', 'criado_em', 'atualizado_em')
    list_editable = ('preco', 'disponivel')
    prepopulated_fields = {'slug': ('nome',)}
    inlines = [VariacaoProdutoInline]

# Opcional: registrar VariacaoProduto separadamente se quiser um gerenciamento mais detalhado
@admin.register(VariacaoProduto)
class VariacaoProdutoAdmin(admin.ModelAdmin):
    list_display = ('produto', 'tamanho', 'estoque')
    list_filter = ('tamanho', 'produto__nome')
    search_fields = ('produto__nome',)
