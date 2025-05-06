from django.contrib import admin
from .models import Cliente, Producto

@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'apellido', 'email', 'telefono', 'fecha_registro')
    search_fields = ('nombre', 'apellido', 'email')

@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'precio', 'cliente', 'fecha_creacion')
    list_filter = ('cliente',)
    search_fields = ('nombre', 'descripcion')