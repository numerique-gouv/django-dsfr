from django import forms
from django.template import Context, Template
from django.test import SimpleTestCase
from django.utils.datastructures import MultiValueDict

from dsfr.forms import DsfrBaseForm
from dsfr.fields import IntegerRangeField
from dsfr.widgets import NumberCursor


class FormFieldTestCase(SimpleTestCase):
    class DummyForm(DsfrBaseForm):
        user_name = forms.CharField(
            label="Nom d’utilisateur",
            max_length=100,
            widget=forms.TextInput(
                attrs={
                    "autocomplete": "username",
                }
            ),
        )

    def test_full_form_works(self):
        rendered = Template("{{form}}").render(
            Context({"form": FormFieldTestCase.DummyForm()})
        )
        self.assertIn("Nom d’utilisateur", rendered)

    def test_correct_field_works(self):
        rendered = Template(
            "{% load dsfr_tags %}{% dsfr_form_field form.user_name %}"
        ).render(Context({"form": FormFieldTestCase.DummyForm()}))
        self.assertIn("Nom d’utilisateur", rendered)

    def test_incorrect_field_raises_error(self):
        with self.assertRaises(AttributeError):
            _rendered = Template(
                "{% load dsfr_tags %}{% dsfr_form_field form.unknown_field %}"
            ).render(Context({"form": FormFieldTestCase.DummyForm()}))


class IntegerRangeFieldTestCase(SimpleTestCase):
    class DummyForm(DsfrBaseForm):
        integer_range_field = IntegerRangeField()

    class DummyFormWithWidgetCustomizations(DsfrBaseForm):
        integer_range_field = IntegerRangeField(
            widget=NumberCursor(extra_classes="fr-range--sm", prefix="~", suffix="%")
        )

    def test_correct_snippet_and_widget_are_rendered(self):
        rendered = Template("{{form}}").render(
            Context({"form": IntegerRangeFieldTestCase.DummyForm()})
        )
        self.assertTrue('class="fr-range-group ' in rendered)
        self.assertTrue('class="fr-range fr-range--double' in rendered)
        self.assertRegex(
            rendered.replace("\n", ""),
            r'<input\s+id="\w+-low"\s+name="integer_range_field"\s+type="range"',
        )
        self.assertRegex(
            rendered.replace("\n", ""),
            r'<input\s+id="\w+-high"\s+name="integer_range_field"\s+type="range"',
        )

    def test_widget_customizations_are_applied(self):
        rendered = Template("{{form}}").render(
            Context(
                {"form": IntegerRangeFieldTestCase.DummyFormWithWidgetCustomizations()}
            )
        )
        self.assertRegex(
            rendered.replace("\n", ""),
            r'class="fr-range fr-range--double fr-range--sm"\s+data-fr-prefix="~"\s+data-fr-suffix="%"',
        )

    def test_clean_returns_a_range(self):
        form = IntegerRangeFieldTestCase.DummyForm(
            data=MultiValueDict({"integer_range_field": ["10", "50"]})
        )
        form.full_clean()
        self.assertEqual(form.cleaned_data["integer_range_field"], range(10, 51))
