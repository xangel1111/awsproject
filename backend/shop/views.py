from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import Cliente, Producto
from .serializers import ClienteSerializer, ProductoSerializer

class ClienteListView(generics.ListAPIView):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer
    permission_classes = [IsAuthenticated]

class ProductoListView(generics.ListAPIView):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer
    permission_classes = [IsAuthenticated]
    
class ProductosPorClienteView(generics.ListAPIView):
    serializer_class = ProductoSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        cliente_id = self.kwargs['cliente_id']
        return Producto.objects.filter(cliente_id=cliente_id)