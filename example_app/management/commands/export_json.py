from django.core.management.base import BaseCommand

import json
from bs4 import BeautifulSoup
from pathlib import Path


class Command(BaseCommand):
    help = "Exports the whole site as a single JSON file."

    STATIC_ROOT = Path("docs", "django-dsfr")

    def handle(self, *args, **options):
        # Path where django-distill puts the documentation
        output = []

        if not self.STATIC_ROOT.is_dir():
            raise FileNotFoundError(
                "The django-distill export directory was not found."
            )

        for file in self.STATIC_ROOT.rglob("*.html"):
            result = self.get_page_content(file)
            if result:
                output.append(result)

        # Export to both the static dump and the regular app
        with open(self.STATIC_ROOT / "search_data.json", "w") as data_file:
            json.dump(output, data_file, indent=4, sort_keys=True)

        with open("example_app/static/json/search_data.json", "w") as data_file:
            json.dump(output, data_file, indent=4, sort_keys=True)

    def get_page_content(self, file: str):
        filename = str(file).split("/")[-2]
        if filename == "django-dsfr":
            filename = "homepage"

        if filename != "search":
            soup = BeautifulSoup(open(file), "lxml")
            title = soup.title.string.replace(
                "— Système de Design de l’État", ""
            ).strip()
            main = soup.find("main")

            if "Non implémenté" not in title:
                return {
                    "filename": filename,
                    "path": str(file)[4:],
                    "title": title,
                    "text": " ".join(main.get_text().split()),
                }
