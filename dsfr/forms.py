from django import forms


class DsfrBaseForm(forms.Form):
    """
    A base form that adds the necessary class on relevant fields
    """

    # These input widgets don't need the fr-input class
    WIDGETS_NO_FR_INPUT = [
        forms.widgets.CheckboxInput,
        forms.widgets.FileInput,
        forms.widgets.ClearableFileInput,
    ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for visible in self.visible_fields():
            print(visible.field.widget)
            if type(visible.field.widget) not in self.WIDGETS_NO_FR_INPUT:
                visible.field.widget.attrs["class"] = "fr-input"
