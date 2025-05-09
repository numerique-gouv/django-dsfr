from django import forms
from django.template import Context, Template
from django.test import SimpleTestCase

from dsfr.forms import DsfrBaseForm
from dsfr.widgets import InlineRadioSelect, InlineCheckboxSelectMultiple


class RadioSelectTestCase(SimpleTestCase):
    class DummyForm(DsfrBaseForm):
        radio_field = forms.ChoiceField(
            choices=(("a", "bla"), ("i", "bli"), ("o", "blo")),
            widget=forms.RadioSelect(),
        )

    class DummyFormWithInlineRadioSelect(DsfrBaseForm):
        radio_field = forms.ChoiceField(
            choices=(("a", "bla"), ("i", "bli"), ("o", "blo")),
            widget=InlineRadioSelect(),
        )

    def test_not_inline(self):
        rendered = Template("{{form}}").render(
            Context({"form": RadioSelectTestCase.DummyForm()})
        )
        self.assertFalse(
            'class="fr-fieldset__element fr-fieldset__element--inline"' in rendered
        )

    def test_inline(self):
        rendered = Template("{{form}}").render(
            Context({"form": RadioSelectTestCase.DummyFormWithInlineRadioSelect()})
        )
        self.assertTrue(
            'class="fr-fieldset__element fr-fieldset__element--inline"' in rendered
        )


class CheckboxSelectMultipleTestCase(SimpleTestCase):
    class DummyForm(DsfrBaseForm):
        checkbox_field = forms.ChoiceField(
            choices=(("a", "bla"), ("i", "bli"), ("o", "blo")),
            widget=forms.CheckboxSelectMultiple(),
        )

    class DummyFormWithInlineCheckboxSelectMultiple(DsfrBaseForm):
        checkbox_field = forms.ChoiceField(
            choices=(("a", "bla"), ("i", "bli"), ("o", "blo")),
            widget=InlineCheckboxSelectMultiple(),
        )

    def test_not_inline(self):
        rendered = Template("{{form}}").render(
            Context({"form": CheckboxSelectMultipleTestCase.DummyForm()})
        )
        self.assertFalse(
            'class="fr-fieldset__element fr-fieldset__element--inline"' in rendered
        )

    def test_inline(self):
        rendered = Template("{{form}}").render(
            Context(
                {
                    "form": CheckboxSelectMultipleTestCase.DummyFormWithInlineCheckboxSelectMultiple()
                }
            )
        )
        self.assertTrue(
            'class="fr-fieldset__element fr-fieldset__element--inline"' in rendered
        )
