from django.urls import path
from .views import ClienteListView, ProductoListView, ProductosPorClienteView

urlpatterns = [
    path('clientes/', ClienteListView.as_view(), name='cliente-list'),
    path('productos/', ProductoListView.as_view(), name='producto-list'),
    path('clientes/<int:cliente_id>/productos/', ProductosPorClienteView.as_view(), name='cliente-productos'),
]