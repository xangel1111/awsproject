from rest_framework import serializers
from .models import Cliente, Producto

class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = ['id', 'nombre', 'descripcion', 'precio', 'fecha_creacion']

class ClienteSerializer(serializers.ModelSerializer):
    productos = ProductoSerializer(many=True, read_only=True)
    
    class Meta:
        model = Cliente
        fields = ['id', 'nombre', 'apellido', 'email', 'telefono', 'fecha_registro', 'productos']
