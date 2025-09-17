from pathlib import Path

import django
from django import forms
from django.forms import Form, BoundField as DjangoBoundField
from django.forms.renderers import DjangoTemplates, get_default_renderer
from django.utils.functional import cached_property


from dsfr.utils import dsfr_input_class_attr


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


class BoundField(DjangoBoundField):
    if django.VERSION < (5, 0):
        """
        Compatibility with Django<5.0
        https://docs.djangoproject.com/en/5.0/ref/forms/api/#django.forms.BoundField.as_field_group
        """

        def as_field_group(self):
            return self.render()

    @property
    def template_name(self):
        template_name = self.field.template_name or getattr(
            self.field.__class__, "template_name", None
        )
        if template_name:
            return template_name

        match self.widget_type:
            case "checkboxinput":
                return "dsfr/form_field_snippets/checkbox_snippet.html"
            case "checkboxselectmultiple" | "inlinecheckboxselectmultiple":
                return "dsfr/form_field_snippets/checkboxselectmultiple_snippet.html"
            case "radioselect" | "inlineradioselect":
                return "dsfr/form_field_snippets/radioselect_snippet.html"
            case "richradioselect":
                return "dsfr/form_field_snippets/richradioselect_snippet.html"
            case "numbercursor":
                return "dsfr/form_field_snippets/numbercursor_snippet.html"
            case "segmentedcontrol":
                return "dsfr/form_field_snippets/segmented_control_snippet.html"
            case _:
                return "dsfr/form_field_snippets/input_snippet.html"

    def label_tag(self, contents=None, attrs=None, label_suffix=None, tag=None):
        if hasattr(self.field.widget, "dsfr_label_attrs"):
            attrs = {**self.field.widget.dsfr_label_attrs, **(attrs or {})}
        return super().label_tag(contents, attrs, label_suffix, tag)


class DsfrBaseForm(Form):
    """
    A base form that adds the necessary classes on relevant fields
    """

    template_name = "dsfr/form_snippet.html"  # type: ignore
    bound_field_class = BoundField

    @property
    def default_renderer(self):
        from django.conf import settings, global_settings

        return (
            DsfrDjangoTemplates  # Settings wasn't modified
            if settings.FORM_RENDERER == global_settings.FORM_RENDERER
            else get_default_renderer()
        )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for visible in self.visible_fields():
            dsfr_input_class_attr(visible)

    if django.VERSION < (5, 2):
        """
        Compatibility with Django<5.2
        https://docs.djangoproject.com/en/5.2/releases/5.2/#simplified-override-of-boundfield
        """

        def __getitem__(self, name):
            try:
                field = self.fields[name]
            except KeyError:
                raise KeyError(
                    "Key '%s' not found in '%s'. Choices are: %s."
                    % (
                        name,
                        self.__class__.__name__,
                        ", ".join(sorted(self.fields)),
                    )
                )
            if name not in self._bound_fields_cache:
                bound_field_class = getattr(
                    self, "bound_field_class", self.bound_field_class
                )
                self._bound_fields_cache[name] = bound_field_class(self, field, name)
            return self._bound_fields_cache[name]

    def set_autofocus_on_first_error(self):
        """
        Sets the autofocus on the first field with an error message.
        Not included in the __init__ by default because it can cause some side effects on
        non-standard fields/forms.
        """
        for field in self.errors.keys():
            self.fields[field].widget.attrs.update({"autofocus": ""})
            break
