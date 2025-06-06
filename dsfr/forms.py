import warnings
from pathlib import Path

from django import forms
from django.forms.renderers import DjangoTemplates, get_default_renderer
from django.utils.functional import cached_property

from .utils import dsfr_input_class_attr


class DsfrDjangoTemplates(DjangoTemplates):
    @cached_property
    def engine(self):
        return self.backend(
            {
                "APP_DIRS": True,
                "DIRS": [
                    Path(__file__).resolve().parent / self.backend.app_dirname,
                    Path(forms.__path__[0]).resolve() / "templates",  # type: ignore
                ],
                "NAME": "djangoforms",
                "OPTIONS": {},
            }  # type: ignore
        )


class DsfrBaseForm(forms.Form):
    """
    A base form that adds the necessary classes on relevant fields
    """

    template_name = "dsfr/form_snippet.html"  # type: ignore

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for visible in self.visible_fields():
            dsfr_input_class_attr(visible)

    @property
    def default_renderer(self):
        from django.conf import settings, global_settings

        return (
            DsfrDjangoTemplates  # Settings wasn't modified
            if settings.FORM_RENDERER == global_settings.FORM_RENDERER
            else get_default_renderer()
        )

    def get_context(self) -> dict:
        from django.conf import settings

        try:
            mark_optional_fields = settings.DSFR_MARK_OPTIONAL_FIELDS
            warnings.warn("""Transitional Django setting DSFR_MARK_OPTIONAL_FIELDS will be removed
            by the next major version of django-dsfr.""")
        except AttributeError:
            mark_optional_fields = False

        if not mark_optional_fields:
            warnings.warn(
                """Marking required form fields is not recommended by DSFR anymore
                (https://www.systeme-de-design.gouv.fr/version-courante/fr/modeles/blocs-fonctionnels/formulaires#champ-obligatoire)
                so the next major version of django-dsfr will stop doing so,
                and mark optional fields instead.
                To get the future behavior, you can set the transitional Django setting DSFR_MARK_OPTIONAL_FIELDS to True,
                or you can override the DSFR_MARK_OPTIONAL_FIELDS context variable of single forms,
                by overriding YourFormClass.get_context()""",
                DeprecationWarning,
            )

        context = super().get_context()
        context.setdefault("DSFR_MARK_OPTIONAL_FIELDS", mark_optional_fields)
        return context

    def set_autofocus_on_first_error(self):
        """
        Sets the autofocus on the first field with an error message.
        Not included in the __init__ by default because it can cause some side effects on
        non-standard fields/forms.
        """
        for field in self.errors.keys():
            self.fields[field].widget.attrs.update({"autofocus": ""})
            break
