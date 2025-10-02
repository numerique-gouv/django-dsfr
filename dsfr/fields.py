from django.core.exceptions import ValidationError
from django.forms.fields import MultiValueField, IntegerField, BooleanField

from .widgets import NumberCursor, Toggle

__all__ = ["IntegerRangeField"]


class IntegerRangeField(MultiValueField):
    widget = NumberCursor

    """
    This Field can be used to combine two identical IntegerFields
    in order to enable the user to select a range with two cursors.
    The combined value returned is a Python range()
    """

    def __init__(
        self, max_value: int = 100, min_value: int = 0, step_size: int = None, **kwargs
    ):
        self.max_value, self.min_value, self.step_size = max_value, min_value, step_size
        super().__init__(
            fields=(
                IntegerField(
                    required=True,
                    max_value=max_value,
                    min_value=min_value,
                    step_size=step_size,
                ),
                IntegerField(
                    required=True,
                    max_value=max_value,
                    min_value=min_value,
                    step_size=step_size,
                ),
            ),
            **kwargs,
        )
        self.widget.is_range = True

    def widget_attrs(self, widget):
        return {"max": self.max_value, "min": self.min_value, "step": self.step_size}

    def compress(self, data_list: list[int]) -> range:
        if len(data_list) != 2:
            raise ValidationError("Ce champ nécessite de saisir deux nombres entiers")
        if self.required and data_list[1] < data_list[0]:
            raise ValidationError(
                "Le second nombre doit être supérieur au premier pour déterminer un intervalle"
            )
        return range(data_list[0], data_list[1] + 1)


class ToggleField(BooleanField):
    widget = Toggle
    template_name = "dsfr/toggle.html"

    def __init__(self, **kwargs):
        kwargs["label_suffix"] = ""
        super().__init__(**kwargs)
        if self.disabled:
            self.widget.attrs.setdefault("disabled", "true")


