from django.contrib import admin
from .models import CategoriaProd, Comprobante, DetalleComprobante,Producto,Cliente
# Register your models here.

class CategoriaProdAdminAdmin(admin.ModelAdmin):
    readonly_fields=('created','updated')
    list_display=('nombre','created','updated')


class ProductoAdmin(admin.ModelAdmin):
    readonly_fields=('created','updated')
    list_display=('nombre','categorias','created','updated')

admin.site.register(CategoriaProd,CategoriaProdAdminAdmin)
admin.site.register(Producto,ProductoAdmin)
admin.site.register(Cliente)
admin.site.register(Comprobante)
admin.site.register(DetalleComprobante)