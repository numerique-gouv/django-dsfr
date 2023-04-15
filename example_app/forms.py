from django import forms
from django.forms import (
    ModelForm,
    inlineformset_factory,
)  # /!\ In order to use formsets

from dsfr.forms import DsfrBaseForm

# /!\ In order to use formsets
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, Field

from example_app.models import Author, Book
from example_app.utils import populate_genre_choices


class ExampleForm(DsfrBaseForm):
    # basic fields
    user_name = forms.CharField(label="Nom d’utilisateur", max_length=100)

    user_email = forms.EmailField(
        label="Adresse électronique",
        help_text="Format attendu : prenom.nom@domaine.fr",
        required=False,
    )

    password = forms.CharField(
        label="Mot de passe", required=False, widget=forms.PasswordInput
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

    """
    Not managed by the DSFR:
    - DateTimeField
    """

    # Booleans and choicefields
    sample_boolean = forms.BooleanField(label="Cochez la case", required=False)

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
        widget=forms.RadioSelect,
    )

    sample_checkbox = forms.ChoiceField(
        label="Cases à cocher",
        required=False,
        choices=[(1, "Premier choix"), (2, "Second choix"), (3, "Troisième choix")],
        widget=forms.CheckboxSelectMultiple,
    )

    # text blocks
    sample_comment = forms.CharField(widget=forms.Textarea, required=False)

    sample_json = forms.JSONField(label="Fichier JSON", required=False)

    # files

    sample_file = forms.FileField(label="Pièce jointe", required=False)

    def clean_sample_number(self):
        sample_number = self.cleaned_data["sample_number"]

        if sample_number < 0:
            raise forms.ValidationError("Merci d’entrer un nombre positif")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.set_autofocus_on_first_error()


class AuthorCreateForm(ModelForm):
    class Meta:
        model = Author
        exclude = []
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


class BookCreateForm(ModelForm):
    class Meta:
        model = Book
        exclude = []
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
