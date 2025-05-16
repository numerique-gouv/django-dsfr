from django.forms.fields import MultiValueField, IntegerField

from .widgets import NumberCursor


class IntegerOnCursorField(IntegerField):
    def __init__(
        self, max_value: int = 100, min_value: int = 1, step_size: int = None, **kwargs
    ):
        super().__init__(
            min_value=min_value,
            max_value=max_value,
            step_size=step_size,
            widget=NumberCursor(
                min_value=min_value, max_value=max_value, step=step_size
            ),
            **kwargs,
        )


class IntegerRangeField(MultiValueField):
    def __init__(
        self,
        max_value: int = 100,
        min_value: int = 1,
        step_size: int = None,
        **kwargs,
    ):
        super().__init__(
            fields=(
                IntegerField(
                    max_value=max_value,
                    min_value=min_value,
                    step_size=step_size,
                ),
                IntegerField(),
            ),
            widget=NumberCursor(
                min_value=min_value,
                max_value=max_value,
                step=step_size,
                is_range=True,
            ),
            **kwargs,
        )

    def compress(self, data_list: list[int] | tuple[int]):
        return range(data_list[0], data_list[1])
