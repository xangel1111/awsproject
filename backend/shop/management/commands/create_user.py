from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from django.db import IntegrityError

class Command(BaseCommand):
    help = 'Crear un usuario para obtener tokens JWT'


#    def add_arguments(self, parser):
#        parser.add_argument('--username', type=str, help='Nombre de usuario')
#        parser.add_argument('--password', type=str, help='Contraseña del usuario')
#        parser.add_argument('--email', type=str, help='Email del usuario')
#        parser.add_argument('--staff', action='store_true', help='¿Es staff?')
#        parser.add_argument('--superuser', action='store_true', help='¿Es superusuario?')

    def handle(self, *args, **options):
        #username = options.get('username')
        #password = options.get('password')
        username = "user01"
        password = "password123"
        email = "user01@gmail.com"
        is_staff = True
        is_superuser = True
        #email = options.get('email', '')
        #is_staff = options.get('staff', True)
        #is_superuser = options.get('superuser', True)
        
        if not username:
            username = input('Nombre de usuario: ')
        
        if not password:
            from getpass import getpass
            password = getpass('Contraseña: ')
            password_confirm = getpass('Confirmar contraseña: ')
            
            if password != password_confirm:
                self.stdout.write(self.style.ERROR('Las contraseñas no coinciden'))
                return
        
        if not email and not options.get('email'):
            email = input('Email (opcional): ')
        
        try:
            if is_superuser:
                user = User.objects.create_superuser(
                    username=username,
                    email=email,
                    password=password
                )
                self.stdout.write(self.style.SUCCESS(f'Superusuario {username} creado exitosamente'))
            else:
                user = User.objects.create_user(
                    username=username,
                    email=email,
                    password=password,
                    is_staff=is_staff
                )
                self.stdout.write(self.style.SUCCESS(f'Usuario {username} creado exitosamente'))
                
            self.stdout.write(self.style.SUCCESS(f'Ahora puedes obtener un token JWT con estas credenciales'))
            
        except IntegrityError:
            self.stdout.write(self.style.ERROR(f'El usuario {username} ya existe'))