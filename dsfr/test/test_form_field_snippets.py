from django import forms
from django.db.models import IntegerChoices
from django.template import Context, Template
from django.test import SimpleTestCase

from dsfr.enums import SegmentedControlChoices
from dsfr.forms import DsfrBaseForm
from dsfr.widgets import (
    InlineRadioSelect,
    InlineCheckboxSelectMultiple,
    SegmentedControl,
)


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


class SegmentedControlTestCase(SimpleTestCase):
    class DummyForm(DsfrBaseForm):
        class ExampleSegmentedControlChoices(IntegerChoices, SegmentedControlChoices):
            ITEM_1 = {
                "value": 1,
                "label": "Item 1",
                "icon": "table-line",
            }
            ITEM_2 = {
                "value": 2,
                "label": "Item 2",
                "icon": "list-unordered",
            }
            ITEM_3 = {
                "value": 3,
                "label": "Item 3",
                "icon": "layout-grid-line",
            }

        checkbox_field = forms.ChoiceField(
            choices=ExampleSegmentedControlChoices.choices,
            widget=SegmentedControl(extended_choices=ExampleSegmentedControlChoices),
        )

    def test_rendered(self):
        rendered = Template("{{form}}").render(
            Context({"form": SegmentedControlTestCase.DummyForm()})
        )
        self.assertTrue('class="fr-segmented__elements"' in rendered)
        self.assertTrue('<label class="fr-icon-table-line fr-label"' in rendered)
