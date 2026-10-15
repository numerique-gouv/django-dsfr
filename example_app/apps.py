from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class ExampleAppConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "example_app"
    verbose_name = _("Example app")
