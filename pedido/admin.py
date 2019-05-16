from django.contrib import admin
from .models import Pedido, Prato, Cliente

# Register your models here.
class AdminPedido(admin.ModelAdmin):
    list_display = ('origem', 'data_pedido', 'quantidade', 'carne_opcao_1', 'carne_opcao_2', 'descricao', 'total')

class AdminPrato(admin.ModelAdmin):
    list_display = ('tipo', 'valor')


admin.site.register(Pedido, AdminPedido)
admin.site.register(Prato, AdminPrato)
admin.site.register(Cliente)
