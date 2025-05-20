from enum import auto

from django import forms
from django.forms import (
    ModelForm,
    inlineformset_factory,
)  # /!\ In order to use formsets
from django.db.models import IntegerChoices


from dsfr.constants import COLOR_CHOICES, COLOR_CHOICES_ILLUSTRATION
from dsfr.enums import RichRadioButtonChoices
from dsfr.fields import IntegerRangeField
from dsfr.forms import DsfrBaseForm

# /!\ In order to use formsets
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, Field

from dsfr.utils import lazy_static
from dsfr.widgets import (
    RichRadioSelect,
    InlineRadioSelect,
    InlineCheckboxSelectMultiple,
    NumberCursor,
)
from example_app.models import Author, Book
from example_app.utils import populate_genre_choices


class ExampleRichChoices(IntegerChoices, RichRadioButtonChoices):
    ITEM_1 = {
        "value": auto(),
        "label": "Item 1",
        "html_label": "<strong>Item 1</strong>",
        "pictogram": lazy_static("img/placeholder.1x1.png"),
    }
    ITEM_2 = {
        "value": auto(),
        "label": "Item 2",
        "html_label": "<strong>Item 2</strong>",
        "pictogram": lazy_static("img/placeholder.1x1.png"),
    }
    ITEM_3 = {
        "value": auto(),
        "label": "Item 3",
        "html_label": "<strong>Item 3</strong>",
        "pictogram": lazy_static("img/placeholder.1x1.png"),
    }


class ExampleForm(DsfrBaseForm):
    # basic fields
    user_name = forms.CharField(
        label="Nom d’utilisateur",
        max_length=100,
        widget=forms.TextInput(
            attrs={
                "autocomplete": "username",
            }
        ),
    )

    user_email = forms.EmailField(
        label="Adresse électronique",
        help_text="Format attendu : <code>prenom.nom@domaine.fr</code>",
        required=False,
        widget=forms.EmailInput(
            attrs={
                "autocomplete": "email",
            }
        ),
    )

    password = forms.CharField(
        label="Mot de passe",
        required=False,
        widget=forms.PasswordInput(
            attrs={
                "autocomplete": "current-password",
            }
        ),
    )

    sample_number = forms.IntegerField(
        label="Nombre entier",
        help_text="Un nombre inférieur à 0 déclenchera un message d’erreur",
    )

    sample_decimal = forms.DecimalField(
        label="Nombre décimal",
        required=False,
    )

    sample_disabled_field = forms.CharField(
        label="Champ désactivé",
        help_text="Ce champ est désactivé",
        max_length=100,
        disabled=True,
        required=False,
    )

    # date and time
    sample_date = forms.DateField(
        label="Date",
        required=False,
        widget=forms.DateInput(attrs={"type": "date"}),
    )

    sample_datetime = forms.DateTimeField(
        label="Date et heure",
        help_text="""Attention, dans Firefox le sélecteur
        <a href="https://bugzilla.mozilla.org/show_bug.cgi?id=1726108" target="_blank">n’affiche que la date</a>.
        Il reste possible de choisir l’heure directement sur la ligne.""",
        required=False,
        widget=forms.DateInput(attrs={"type": "datetime-local"}),
    )

    # Booleans and choicefields
    sample_boolean = forms.BooleanField(label="Cochez la case", required=True)

    sample_select = forms.ChoiceField(
        label="Liste déroulante",
        required=False,
        choices=[(1, "Option 1"), (2, "Option 2"), (3, "Option 3")],
    )

    sample_multiple_select = forms.MultipleChoiceField(
        label="Liste déroulante à choix multiples",
        required=False,
        choices=[(1, "Option 1"), (2, "Option 2"), (3, "Option 3")],
    )

    sample_radio = forms.ChoiceField(
        label="Boutons radio",
        required=False,
        choices=[(1, "Premier choix"), (2, "Second choix"), (3, "Troisième choix")],
        help_text="Le troisième choix renvoie une erreur s’il est sélectionné",
        widget=forms.RadioSelect,
    )

    sample_radio_inline = forms.ChoiceField(
        label="Boutons radio inline",
        required=False,
        choices=[(1, "Premier choix"), (2, "Second choix"), (3, "Troisième choix")],
        widget=InlineRadioSelect,
    )

    sample_checkbox = forms.MultipleChoiceField(
        label="Cases à cocher",
        required=False,
        choices=[
            ("1", "Premier choix"),
            ("2", "Second choix"),
            ("3", "Troisième choix"),
        ],
        help_text="Le troisième choix renvoie une erreur s’il est sélectionné",
        widget=forms.CheckboxSelectMultiple,
    )

    sample_checkbox_inline = forms.MultipleChoiceField(
        label="Cases à cocher inline",
        required=False,
        choices=[
            ("1", "Premier choix"),
            ("2", "Second choix"),
            ("3", "Troisième choix"),
        ],
        widget=InlineCheckboxSelectMultiple,
    )

    sample_rich_radio = forms.ChoiceField(
        label="Boutons radio riche",
        required=False,
        choices=ExampleRichChoices.choices,
        help_text="Exemple de boutons radios riches",
        widget=RichRadioSelect(rich_choices=ExampleRichChoices),
    )

    inline_rich_radio = forms.ChoiceField(
        label="Boutons radio riche en ligne",
        required=False,
        choices=ExampleRichChoices.choices,
        help_text="Exemple de boutons radios riches en ligne",
        widget=RichRadioSelect(rich_choices=ExampleRichChoices, inline=True),
    )

    # text blocks
    sample_comment = forms.CharField(widget=forms.Textarea, required=False)

    sample_json = forms.JSONField(label="Fichier JSON", required=False)

    # files
    sample_file = forms.FileField(label="Pièce jointe", required=False)

    # range
    sample_integer_with_cursor = forms.IntegerField(
        label="Nombre à choisir avec un curseur, simple, requis",
        help_text="Texte de description additionnel",
        required=True,
        widget=NumberCursor(),
    )
    sample_integer_with_cursor_disabled = forms.IntegerField(
        label="Nombre à choisir avec un curseur, désactivé",
        help_text="Texte de description additionnel",
        required=False,
        disabled=True,
        widget=NumberCursor(),
    )
    sample_integer_with_cursor_with_steps = forms.IntegerField(
        label="Nombre à choisir dans un intervalle explicite, avec un curseur cranté de 5 en 5, petite taille, avec préfixe et suffixe",
        help_text="Texte de description additionnel",
        required=False,
        max_value=70,
        min_value=10,
        step_size=5,
        widget=NumberCursor(extra_classes="fr-range--sm", prefix="~", suffix="%"),
    )
    sample_integer_range = IntegerRangeField(
        label="Intervalle de nombres",
        help_text="Déplacez les curseurs pour choisir un intervalle",
        required=False,
    )
    sample_integer_range_small = IntegerRangeField(
        label="Intervalle de nombres, petite taille, suffixe",
        help_text="Déplacez les curseurs pour choisir un intervalle de prix",
        required=False,
        max_value=70,
        min_value=10,
        widget=NumberCursor(extra_classes="fr-range--sm", suffix="€"),
    )

    # hidden field
    hidden_input = forms.CharField(widget=forms.HiddenInput(), initial="value")

    def clean_sample_number(self):
        sample_number = self.cleaned_data["sample_number"]

        if sample_number < 0:
            raise forms.ValidationError("Merci d’entrer un nombre positif")

        return sample_number

    def clean_sample_radio(self):
        sample_radio = self.cleaned_data["sample_radio"]

        if sample_radio == "3":
            raise forms.ValidationError("Le troisième choix est interdit")

        return sample_radio

    def clean_sample_checkbox(self):
        sample_checkbox = self.cleaned_data["sample_checkbox"]

        if "3" in sample_checkbox:
            raise forms.ValidationError("Le troisième choix est interdit")

        return sample_checkbox

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.set_autofocus_on_first_error()


class AuthorCreateForm(ModelForm, DsfrBaseForm):
    class Meta:
        model = Author
        exclude = []  # NOSONAR
        widgets = {
            "first_name": forms.TextInput(),
            "last_name": forms.TextInput(),
            "birth_date": forms.DateInput(
                attrs={
                    "type": "date",
                }
            ),
        }


# If you need to define help_text for one radio button or checkbox in particular, you can do it in a dict {'label':...., 'help_text':....}
BOOK_FORMAT = (
    ("PAPER", "Papier"),
    ("NUM", {"label": "Numérique", "help_text": "Livre électronique"}),
)


class BookCreateForm(ModelForm, DsfrBaseForm):
    class Meta:
        model = Book
        exclude = []  # NOSONAR
        widgets = {
            "title": forms.TextInput(),
            "number_of_pages": forms.NumberInput(),
        }

    # /!\ You have to redefine each radio buttons or checkboxes field like so :
    book_format = forms.ChoiceField(
        label="Format",
        choices=BOOK_FORMAT,  # If the choices are in a constant
        widget=forms.RadioSelect(attrs={"class": "fr-fieldset--inline"}),
    )

    # /!\ Genre is a model, but it requires to format the list of object before passing to the field
    # Using a ModelMultipleChoiceField won't show individual help_texts under each checkbox
    # I declared a variable GENRES in order to show individual help_texts
    genre = forms.MultipleChoiceField(
        label="Genre",
        choices=populate_genre_choices,
        widget=forms.CheckboxSelectMultiple(),
        required=False,
        help_text="Veuillez choisir le ou les genres associés au livre",
    )

    def clean(self):
        cleaned_data = super().clean()
        return cleaned_data


# /!\ In order to use formsets, you have to define a crispy FormHelper for the form used for the formset
class BookCreateFormHelper(FormHelper):
    def __init__(self, *args, **kwargs):
        super(BookCreateFormHelper, self).__init__(*args, **kwargs)
        # self.form_tag = False
        self.layout = Layout(
            Fieldset(
                "Ajouter un livre",
                Field("title"),
                Field("number_of_pages"),
                Field("book_format"),
                Field("genre"),
            ),
        )


# /!\ In order to use formsets, you have to define an formset factory
BookCreateFormSet = inlineformset_factory(
    Author,
    Book,
    form=BookCreateForm,
    extra=1,
    exclude=[],
)


class AccentColorForm(DsfrBaseForm):
    color_accent = forms.ChoiceField(
        label="Choisissez une couleur",
        required=False,
        choices=[("", "----")] + COLOR_CHOICES_ILLUSTRATION,
    )


class FullColorForm(DsfrBaseForm):
    color_full = forms.ChoiceField(
        label="Choisissez une couleur",
        required=False,
        choices=[("", "----")] + COLOR_CHOICES,
    )
