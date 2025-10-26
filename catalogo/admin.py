from django.contrib import admin
from .models import Filme, Avaliacao

# Register your models here.
@admin.register(Filme)
class FilmeAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'url', 'criacao', 'atualizacao', 'ativo')

@admin.register(Avaliacao)
class AvaliacaoAdmin(admin.ModelAdmin):
    list_display = ('filme', 'nome', 'email', 'avaliacao', 'criacao', 'atualizacao', 'ativo')

