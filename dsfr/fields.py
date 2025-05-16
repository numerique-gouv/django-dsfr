from django.core.exceptions import ValidationError
from django.forms.fields import MultiValueField, IntegerField

from .widgets import NumberCursor


class IntegerOnCursorField(IntegerField):
    """
    This Field adds no validation logic to IntegerField,
    it just passes IntegerField options to the NumberCursor widget
    """

    def __init__(
        self, max_value: int = 100, min_value: int = 1, step_size: int = None, **kwargs
    ):
        super().__init__(
            max_value=max_value,
            min_value=min_value,
            step_size=step_size,
            widget=NumberCursor(),
            **kwargs,
        )


class IntegerRangeField(MultiValueField):
    """
    This Field can be used to combine two identical IntegerFields
    in order to enable the user to select a range with two cursors.
    The combined value returned is a Python range()
    """

    def __init__(
        self, max_value: int = 100, min_value: int = 1, step_size: int = None, **kwargs
    ):
        self.max_value = max_value
        self.min_value = min_value
        self.step_size = step_size
        super().__init__(
            fields=(
                IntegerField(
                    max_value=max_value,
                    min_value=min_value,
                    step_size=step_size,
                ),
                IntegerField(
                    max_value=max_value,
                    min_value=min_value,
                    step_size=step_size,
                ),
            ),
            widget=NumberCursor(
                min_value=min_value,
                max_value=max_value,
                step=step_size,
                is_range=True,
            ),
            **kwargs,
        )

    def compress(self, data_list: list[int] | tuple[int]) -> range:
        return range(data_list[0], data_list[1])

    def clean(self, value):
        value = super().clean(value)
        if not isinstance(value, range):
            raise ValidationError("IntegerRangeField value must be a range")
        if not len(value):
            raise ValidationError("IntegerRangeField value must be a non-empty range")
        return value
