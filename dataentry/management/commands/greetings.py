from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help="Greetings Command"

    def handle(self, *args, **options):
        self.stdout.write("Greetings Siva")