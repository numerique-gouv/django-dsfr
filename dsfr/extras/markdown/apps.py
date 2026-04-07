from importlib.util import find_spec

from django.apps import AppConfig


class DsfrMarkdownConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "dsfr.extras.markdown"

    def ready(self):
        for dep in ("markdown", "pymdownx", "lxml"):
            if find_spec(dep) is None:
                raise ImportError(
                    f"No module named {dep}; to use django-dsfr's markdown features, you must install the 'markdown' feature by specifying 'django-dsfr[markdown]' in your requirements.txt or pyproject.toml"
                )
        super().ready()
