from pathlib import Path

from django import forms
from django.forms.renderers import DjangoTemplates, get_default_renderer
from django.utils.functional import cached_property

from . import settings as dsfr_settings
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

    def get_context(self):
        context = super().get_context()

        context.update({"DSFR_MARK_FORM_FIELDS": dsfr_settings.mark_form_fields})

        return context

    @property
    def default_renderer(self):
        from django.conf import settings, global_settings

        return (
            DsfrDjangoTemplates  # Settings wasn't modified
            if settings.FORM_RENDERER == global_settings.FORM_RENDERER
            else get_default_renderer()
        )

    def set_autofocus_on_first_error(self):
        """
        Sets the autofocus on the first field with an error message.
        Not included in the __init__ by default because it can cause some side effects on
        non-standard fields/forms.
        """
        for field in self.errors.keys():
            self.fields[field].widget.attrs.update({"autofocus": ""})
            break
