import os
from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model

class Command(BaseCommand):
    help = 'Creates a superuser with predefined credentials if none exists'

    def handle(self, *args, **options):
        User = get_user_model()
        if not User.objects.filter(is_superuser=True).exists():
            # Get credentials from environment variables
            username = os.environ.get('DJANGO_SUPERUSER_USERNAME')
            email = os.environ.get('DJANGO_SUPERUSER_EMAIL')
            password = os.environ.get('DJANGO_SUPERUSER_PASSWORD')

            # Check if all required credentials are provided
            if not all([username, email, password]):
                self.stdout.write(self.style.ERROR(
                    'Missing required environment variables for superuser creation'
                ))
                return

            try:
                superuser = User.objects.create_superuser(
                    username=username,
                    email=email,
                    password=password
                )
                self.stdout.write(self.style.SUCCESS(
                    f'Superuser created successfully with username: {username}'
                ))
            except Exception as e:
                self.stdout.write(self.style.ERROR(
                    f'Error creating superuser: {str(e)}'
                ))
        else:
            self.stdout.write(self.style.WARNING('Superuser already exists'))