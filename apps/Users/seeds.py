from django.contrib.auth.models import Group, Permission
from django.core.management.base import BaseCommand


'''class Command(BaseCommand):
    def handle(self, *args, **options):
        # Crear grupo de administradores y asignar permisos
        admin_group, _ = Group.objects.get_or_create(name='Administradores')
        admin_group.permissions.add(Permission.objects.get(codename='crear_permiso'))
        admin_group.permissions.add(Permission.objects.get(codename='eliminar_permiso'))
        # Agrega otros permisos necesarios

        # Crear grupo de usuarios estándar y asignar permisos
        user_group, _ = Group.objects.get_or_create(name='Usuarios Estándar')
        user_group.permissions.add(Permission.objects.get(codename='leer_permiso'))
        user_group.permissions.add(Permission.objects.get(codename='actualizar_permiso'))
        # Agrega otros permisos necesarios
'''
