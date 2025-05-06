import random
from django.core.management.base import BaseCommand
from django.db import transaction
from faker import Faker
from shop.models import Cliente, Producto

class Command(BaseCommand):
    help = 'Generar datos de prueba para clientes y productos'

    def add_arguments(self, parser):
        parser.add_argument('--clientes', type=int, default=10, help='Número de clientes a generar')
        parser.add_argument('--productos', type=int, default=5, help='Número de productos por cliente')
        parser.add_argument('--eliminar', action='store_true', help='Eliminar datos existentes antes de generar nuevos')

    def handle(self, *args, **options):
        num_clientes = options['clientes']
        productos_por_cliente = options['productos']
        eliminar = options['eliminar']
        
        faker = Faker('es_ES')  # Usar locale español
        
        self.stdout.write(self.style.SUCCESS(f'Iniciando generación de {num_clientes} clientes con {productos_por_cliente} productos cada uno...'))
        
        if eliminar:
            self.stdout.write(self.style.WARNING('Eliminando datos existentes...'))
            Producto.objects.all().delete()
            Cliente.objects.all().delete()
            self.stdout.write(self.style.SUCCESS('Datos eliminados correctamente.'))
        
        # Usar transacción para mejorar rendimiento y asegurar consistencia
        with transaction.atomic():
            # Crear clientes
            clientes_creados = []
            for _ in range(num_clientes):
                cliente = Cliente.objects.create(
                    nombre=faker.first_name(),
                    apellido=faker.last_name(),
                    email=faker.email(),
                    telefono=faker.phone_number()[:15],  # Limitar a 15 caracteres según el modelo
                )
                clientes_creados.append(cliente)
                
            self.stdout.write(self.style.SUCCESS(f'Se han creado {len(clientes_creados)} clientes.'))
            
            # Crear productos para cada cliente
            total_productos = 0
            categorias = ['Electrónica', 'Ropa', 'Hogar', 'Deportes', 'Juguetes', 'Libros', 'Alimentos']
            
            for cliente in clientes_creados:
                for _ in range(productos_por_cliente):
                    # Generar un precio aleatorio entre 10 y 1000
                    precio = round(random.uniform(10, 1000), 2)
                    categoria = random.choice(categorias)
                    
                    Producto.objects.create(
                        nombre=f"{categoria} - {faker.word().capitalize()}",
                        descripcion=faker.paragraph(),
                        precio=precio,
                        cliente=cliente
                    )
                    total_productos += 1
            
            self.stdout.write(self.style.SUCCESS(f'Se han creado {total_productos} productos.'))
        
        self.stdout.write(self.style.SUCCESS('¡Proceso de generación de datos completado con éxito!'))