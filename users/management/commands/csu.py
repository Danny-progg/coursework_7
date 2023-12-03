from django.core.management import BaseCommand

from users.models import User


class Command(BaseCommand):
    def handle(self, *args, **options):
        user = User.objects.create(
            email="daniilmurzin333@gmail.com",
            first_name="Daniil",
            last_name="Murzin",
            is_superuser=True,
            is_staff=True,
            is_active=True,
        )

        user.set_password("852799")
        user.save()