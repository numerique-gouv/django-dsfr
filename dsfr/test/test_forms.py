from typing import NoReturn

from django import forms
from django.test import SimpleTestCase


from dsfr.forms import DsfrBaseForm


class DsfrBaseFormTestCase(SimpleTestCase):
    class TestForm(DsfrBaseForm):
        book_format = forms.ChoiceField(
            label="Format",
            choices=(
                ("PAPER", "Papier"),
                ("NUM", "Numérique"),
            ),
        )
        book_format2 = forms.ChoiceField(
            label="Format",
            choices=(
                ("PAPER", "Papier"),
                ("NUM", "Numérique"),
            ),
            widget=forms.RadioSelect,
        )
        user_id = forms.CharField(widget=forms.HiddenInput)

    def test_init_sets_attributes(self):
        form = self.TestForm(data={})
        self.assertEqual(form.fields["book_format"].widget.attrs["class"], "fr-select")
        self.assertEqual(
            form.fields["book_format"].widget.group_class, "fr-select-group"
        )
        self.assertEqual(form.fields["book_format2"].widget.attrs["dsfr"], "dsfr")
        self.assertEqual(
            form.fields["book_format2"].widget.group_class, "fr-radio-group"
        )
        self.assertEqual(form.fields["user_id"].widget.attrs, {})

    def test_init_dont_trigger_form_validation(self):
        test_ctx = self

        class AssertForm(self.TestForm):
            @property
            def errors(self) -> NoReturn:
                test_ctx.fail("No validation expected")

        # __init__ should not trigger validation
        AssertForm(data={})

        with self.assertRaises(self.failureException):
            # is_valid should trigger validation
            AssertForm(data={}).is_valid()
