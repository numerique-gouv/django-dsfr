from django.core.management.base import BaseCommand

from example_app.models import Genre


class Command(BaseCommand):
    help = "Add some sample data to be able to test the forms."

    def handle(self, *args, **options):
        # Note: the command should be able to be run several times without creating
        # duplicate objects.
        Genre.objects.get_or_create(code="SF", designation="Science-Fiction")
        Genre.objects.get_or_create(
            code="FTSQUE",
            designation="Fantastique",
            help_text="Intrusion du surnaturel dans un cadre réaliste",
        )
        Genre.objects.get_or_create(
            code="FTSY",
            designation="Fantasy",
            help_text="Élaboration d’un univers distinct du monde réel",
        )
