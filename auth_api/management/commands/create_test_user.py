from django.core.management.base import BaseCommand
from django.contrib.auth.models import User

class Command(BaseCommand):
    help = 'Creates a test user for development'

    def handle(self, *args, **kwargs):
        username = 'testuser'
        password = 'testpass123'
        
        if User.objects.filter(username=username).exists():
            self.stdout.write(self.style.WARNING(f'User {username} already exists'))
            return

        User.objects.create_user(username=username, password=password)
        self.stdout.write(self.style.SUCCESS(f'Successfully created test user: {username}')) 