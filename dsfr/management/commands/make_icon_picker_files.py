from django.core.management.base import BaseCommand
import json
import os

from dsfr.utils import dsfr_version


class Command(BaseCommand):
    help = "Add some initial sample data for the example app."

    def handle(self, *args, **options):
        # Note: the command should be able to be run several times without creating
        # duplicate objects.
        icons_root = "dsfr/static/dsfr/dist/icons/"
        icons_folders = os.listdir(icons_root)
        icons_folders.sort()

        json_root = "dsfr/static/django-dsfr/icon-picker/assets/icons-libraries/"

        all_folders = []

        for folder in icons_folders:
            icons_dict = {
                "prefix": "fr-icon-",
                "version": dsfr_version(),
                "icons": [],
            }

            files = os.listdir(os.path.join(icons_root, folder))
            files_without_extensions = [
                f.split(".")[0].replace("fr--", "") for f in files
            ]
            files_without_extensions.sort()

            dsfr_folder = f"dsfr-{folder}"
            dsfr_folder_json = dsfr_folder + ".json"
            icons_dict["icons"] = files_without_extensions
            icons_dict["icon-style"] = dsfr_folder
            icons_dict["list-label"] = f"DSFR {folder.title()}"

            all_folders.append(dsfr_folder_json)

            json_file = os.path.join(json_root, dsfr_folder_json)
            with open(json_file, "w") as fp:
                json.dump(icons_dict, fp)
                fp.write("\n")

        self.stdout.write(
            self.style.SUCCESS("Folders created or updated: ", all_folders)
        )
