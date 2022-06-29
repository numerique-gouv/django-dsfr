from django import forms
from dsfr.forms import DsfrBaseForm


class ExampleForm(DsfrBaseForm):
    # basic fields
    user_name = forms.CharField(label="Votre nom", max_length=100)

    user_email = forms.EmailField(label="Votre courriel", required=False)

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
