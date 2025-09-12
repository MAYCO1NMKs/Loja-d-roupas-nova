from django.contrib import admin
from .models import Categoria, Produto, Cor, Tamanho

# Register your models here.

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('nome',)

@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'categoria', 'preco', 'disponivel', 'imagem')
    list_filter = ('disponivel', 'categoria')
    search_fields = ('nome', 'descricao')

@admin.register(Cor)
class CorAdmin(admin.ModelAdmin):
    list_display = ('nome',)

@admin.register(Tamanho)
class TamanhoAdmin(admin.ModelAdmin):
    list_display = ('nome',)
