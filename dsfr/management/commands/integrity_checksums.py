import base64
import hashlib
from pathlib import Path

from django.core.management.base import BaseCommand
from black import format_str, FileMode


class Command(BaseCommand):
    help = "Updates the integrity checksums for the css/js/favicon files."

    BASE_PATH = Path("dsfr/static/dsfr/dist")

    def handle(self, *args, **options):
        files = [
            {"path": "dsfr/dsfr.module.min.js", "constant": "INTEGRITY_JS_MODULE"},
            {"path": "dsfr/dsfr.nomodule.min.js", "constant": "INTEGRITY_JS_NOMODULE"},
            {"path": "dsfr/dsfr.min.css", "constant": "INTEGRITY_CSS"},
            {"path": "utility/utility.min.css", "constant": "INTEGRITY_UTILITY_CSS"},
        ]

        output_text = """# Integrity checks for the css/js/favicon files
# Do not update manually!
# Generated with the following command:
# python manage.py integrity_checksums\n\n"""

        for file in files:
            constant = file["constant"]
            file_path = self.BASE_PATH / file["path"]

            with open(file_path, "rb") as f:
                content = f.read()
                checksum = self.calculate_checksum(content)

            output_text += f"# {file_path}\n"
            output_text += f'{constant} = ("{checksum}")\n\n'

        output_text = format_str(output_text, mode=FileMode())
        with open("dsfr/checksums.py", "w") as output_file:
            output_file.write(output_text)

    def calculate_checksum(self, input_content: bytes):
        hashed_content = hashlib.sha384(input_content).digest()
        hash_base64 = base64.b64encode(hashed_content).decode()
        return "sha384-{}".format(hash_base64)
