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
            """
            Depending on the widget, we have to add some classes:
            - on the outer group
            - on the form field itsef

            If a class is already set, we don't force the DSFR-specific classes.
            """
            if "class" not in visible.field.widget.attrs:
                if type(visible.field.widget) in [
                    forms.widgets.Select,
                    forms.widgets.SelectMultiple,
                ]:
                    visible.field.widget.attrs["class"] = "fr-select"
                    visible.field.widget.group_class = "fr-select-group"
                elif type(visible.field.widget) == forms.widgets.RadioSelect:
                    visible.field.widget.group_class = "fr-radio-group"
                elif type(visible.field.widget) == forms.widgets.CheckboxSelectMultiple:
                    visible.field.widget.attrs["dsfr"] = "dsfr"
                elif type(visible.field.widget) not in self.WIDGETS_NO_FR_INPUT:
                    visible.field.widget.attrs["class"] = "fr-input"

    def set_autofocus_on_first_error(self):
        """
        Sets the autofocus on the first field with an error message.
        Not included in the __init__ by default because it can cause some side effects on
        non-standard fields/forms.
        """
        for field in self.errors.keys():
            self.fields[field].widget.attrs.update({"autofocus": ""})
            break
