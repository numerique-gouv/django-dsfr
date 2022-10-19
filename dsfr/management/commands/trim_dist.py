import os
from glob import glob

from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "Removes extra files from the dsfr/dist folder in order to save space."

    BASE_PATH = "dsfr/static/dsfr/dist"

    def handle(self, *args, **options):
        print("Delete CSS map files and non-minified CSS files")
        deleted_files = 0
        all_css_map_files = self.get_files_by_ext("*.css.map")
        for file in all_css_map_files:
            os.remove(file)
            deleted_files += 1

        all_full_css_files = self.get_non_minified_files_by_ext("*.css", ".min.css")
        for file in all_full_css_files:
            os.remove(file)
            deleted_files += 1

        print(f"{deleted_files} files deleted.")

        print("Delete JS map files and non-minified files")
        deleted_files = 0
        all_js_map_files = self.get_files_by_ext("*.js.map")
        for file in all_js_map_files:
            os.remove(file)
            deleted_files += 1

        all_full_js_files = self.get_non_minified_files_by_ext("*.js", ".min.js")
        for file in all_full_js_files:
            os.remove(file)
            deleted_files += 1

        print(f"{deleted_files} files deleted.")

        print("Removing mentions of deleted files")
        edited_files = 0
        all_minified_js_files = self.get_files_by_ext("*.min.js")
        for filename in all_minified_js_files:
            with open(filename, "r+") as file:
                original_content = file.readlines()
                file.seek(0)
                for line in original_content:
                    if "//# sourceMappingURL=" not in line:
                        file.write(line)
                file.truncate()
                edited_files += 1

        print(f"{edited_files} files edited.")

    def get_files_by_ext(self, extension) -> list:
        return [
            filename
            for path, directories, filenames in os.walk(self.BASE_PATH)
            for filename in glob(os.path.join(path, extension))
        ]

    def get_non_minified_files_by_ext(self, extension, minified_extension) -> list:
        return [
            filename
            for path, directories, filenames in os.walk(self.BASE_PATH)
            for filename in glob(os.path.join(path, extension))
            if not filename.endswith(minified_extension)
        ]
