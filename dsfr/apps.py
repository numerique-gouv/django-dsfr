from django.apps import AppConfig


class DsfrConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"  # type: ignore
    name = "dsfr"
    verbose_name = "Système de design de l’État"
