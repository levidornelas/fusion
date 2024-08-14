from django.contrib import admin
from .models import Funcionario, Cargo, Servico, Preco, Testemunho
# Register your models here.

@admin.register(Cargo)
class CargoAdmin(admin.ModelAdmin):
  list_display = 'cargo', 'modificado', 'ativo'

@admin.register(Servico)
class ServicoAdmin(admin.ModelAdmin):
  list_display = 'servico', 'icone', 'ativo', 'modificado'

@admin.register(Funcionario)
class FuncionarioAdmin(admin.ModelAdmin):
  list_display = 'nome', 'cargo', 'ativo', 'modificado'

@admin.register(Preco)
class PrecosAdmin(admin.ModelAdmin):
  list_display = 'preco', 'titulo', 'descricao'

@admin.register(Testemunho)
class TestemunhoAdmin(admin.ModelAdmin):
  list_display = 'nome', 'ocupacao', 'descricao', 'imagem', 'estrelas'