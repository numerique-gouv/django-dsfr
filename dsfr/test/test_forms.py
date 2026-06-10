from typing import NoReturn

from django import forms
from django.test import SimpleTestCase

from dsfr.enums import RichRadioButtonChoices
from dsfr.forms import DsfrBaseForm
from dsfr.widgets import (
    InlineCheckboxSelectMultiple,
    InlineRadioSelect,
    RichRadioSelect,
    NumberCursor,
    SegmentedControl,
)


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


class WidgetsTest(DsfrBaseFormTestCase):
    maxDiff = None

    def _create_form_with_widget(
        self, widget: forms.Widget | type[forms.Widget]
    ) -> DsfrBaseForm:
        klass = type(
            f"{widget.__class__.__name__}Form",
            (DsfrBaseForm,),
            {"input": forms.Field(widget=widget)},
        )
        return klass()

    def _create_form_with_fields(self, fields: dict[str, forms.Field]) -> DsfrBaseForm:
        return type("TestForm", (DsfrBaseForm,), fields)()

    def test_template_name(self):
        form = self._create_form_with_widget(forms.CheckboxInput)
        self.assertEqual(
            "dsfr/form_field_snippets/checkbox_snippet.html",
            form["input"].template_name,
        )

        form = self._create_form_with_widget(forms.CheckboxSelectMultiple)
        self.assertEqual(
            "dsfr/form_field_snippets/checkboxselectmultiple_snippet.html",
            form["input"].template_name,
        )

        form = self._create_form_with_widget(InlineCheckboxSelectMultiple)
        self.assertEqual(
            "dsfr/form_field_snippets/checkboxselectmultiple_snippet.html",
            form["input"].template_name,
        )

        form = self._create_form_with_widget(forms.RadioSelect)
        self.assertEqual(
            "dsfr/form_field_snippets/radioselect_snippet.html",
            form["input"].template_name,
        )

        form = self._create_form_with_widget(InlineRadioSelect)
        self.assertEqual(
            "dsfr/form_field_snippets/radioselect_snippet.html",
            form["input"].template_name,
        )

        class ExampleRichChoices(RichRadioButtonChoices):
            pass

        form = self._create_form_with_widget(
            RichRadioSelect(extended_choices=ExampleRichChoices)
        )
        self.assertEqual(
            "dsfr/form_field_snippets/richradioselect_snippet.html",
            form["input"].template_name,
        )

        form = self._create_form_with_widget(NumberCursor)
        self.assertEqual(
            "dsfr/form_field_snippets/numbercursor_snippet.html",
            form["input"].template_name,
        )

        form = self._create_form_with_widget(
            SegmentedControl(extended_choices=ExampleRichChoices)
        )
        self.assertEqual(
            "dsfr/form_field_snippets/segmented_control_snippet.html",
            form["input"].template_name,
        )

    def test_render_checkbox(self):
        # language=html
        html = """
            <div class="fr-checkbox-group fr-mb-2w">
                <input type="checkbox" id="id_storybook" name="storybook" required>
                <label class="fr-label" for="id_storybook">
                    libellé radio<span aria-hidden="true" class="fr-required-marker">*</span>
                </label>
            </div>
        """

        form = self._create_form_with_fields(
            {"storybook": forms.BooleanField(label="libellé radio")}
        )
        self.assertHTMLEqual(html, form["storybook"].as_field_group())

    def test_render_checkbox_multiple(self):
        # language=html
        html = """
            <fieldset class="fr-fieldset fr-fieldsets" id="checkboxes-id_storybook" aria-labelledby="id_storybook-legend">
              <legend class="fr-fieldset__legend--regular fr-fieldset__legend" id="id_storybook-legend">
                  Légende pour l’ensemble des éléments<span aria-hidden="true" class="fr-required-marker">*</span>
              </legend>
              <div class="fr-fieldset__element">
                <div class="fr-checkbox-group">
                  <input dsfr="dsfr" name="storybook" id="id_storybook_0" type="checkbox" value="checkbox1">
                  <label class="fr-label" for="id_storybook_0"> Checkbox 1 </label>
                </div>
              </div>
              <div class="fr-fieldset__element">
                <div class="fr-checkbox-group">
                  <input dsfr="dsfr" name="storybook" id="id_storybook_1" type="checkbox" value="checkbox2">
                  <label class="fr-label" for="id_storybook_1"> Checkbox 2 </label>
                </div>
              </div>
              <div class="fr-fieldset__element">
                <div class="fr-checkbox-group">
                  <input dsfr="dsfr" name="storybook" id="id_storybook_2" type="checkbox" value="checkbox3">
                  <label class="fr-label" for="id_storybook_2"> Checkbox 3 </label>
                </div>
              </div>
            </fieldset>
        """

        form = self._create_form_with_fields(
            {
                "storybook": forms.ChoiceField(
                    label="Légende pour l’ensemble des éléments",
                    choices=(
                        ("checkbox1", "Checkbox 1"),
                        ("checkbox2", "Checkbox 2"),
                        ("checkbox3", "Checkbox 3"),
                    ),
                    widget=forms.CheckboxSelectMultiple,
                )
            }
        )
        self.assertHTMLEqual(html, form["storybook"].as_field_group())

    def test_render_select_multiple(self):
        # language=html
        html = """
               <fieldset class="fr-fieldset" id="radio-id_storybook" aria-labelledby="id_storybook-legend">
                   <legend class="fr-fieldset__legend--regular fr-fieldset__legend" id="id_storybook-legend">
                       Légende pour l’ensemble des éléments<span aria-hidden="true" class="fr-required-marker">*</span>
                   </legend>
                   <div class="fr-fieldset__element">
                       <div class="fr-radio-group">
                           <input dsfr="dsfr" type="radio" id="id_storybook_0" name="storybook" value="radio1" required>
                           <label class="fr-label" for="id_storybook_0"> Radio 1 </label>
                       </div>
                   </div>
                   <div class="fr-fieldset__element">
                       <div class="fr-radio-group">
                           <input dsfr="dsfr" type="radio" id="id_storybook_1" name="storybook" value="radio2" required>
                           <label class="fr-label" for="id_storybook_1"> Radio 2 </label>
                       </div>
                   </div>
                   <div class="fr-fieldset__element">
                       <div class="fr-radio-group">
                           <input dsfr="dsfr" type="radio" id="id_storybook_2" name="storybook" value="radio3" required>
                           <label class="fr-label" for="id_storybook_2"> Radio 3 </label>
                       </div>
                   </div>
               </fieldset> \
               """

        form = self._create_form_with_fields(
            {
                "storybook": forms.ChoiceField(
                    label="Légende pour l’ensemble des éléments",
                    choices=(
                        ("radio1", "Radio 1"),
                        ("radio2", "Radio 2"),
                        ("radio3", "Radio 3"),
                    ),
                    widget=forms.RadioSelect,
                )
            }
        )
        self.assertHTMLEqual(html, form["storybook"].as_field_group())
