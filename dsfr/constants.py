from django.utils.translation import gettext_lazy as _

# List of languages for which the interface translation is currently available
DJANGO_DSFR_LANGUAGES = [
    ("en", _("English")),
    ("fr", _("French")),
]

# Color palettes, per https://www.systeme-de-design.gouv.fr/elements-d-interface/fondamentaux-de-l-identite-de-l-etat/couleurs-palette/

COLOR_CHOICES_PRIMARY = [
    ("blue-france", _("Blue France")),
    ("red-marianne", _("Red Marianne")),
]

COLOR_CHOICES_NEUTRAL = [
    ("grey", _("Grey")),
]

COLOR_CHOICES_SYSTEM = [
    ("info", _("Info")),
    ("success", _("Success")),
    ("warning", _("Warning")),
    ("error", _("Error")),
]

COLOR_CHOICES_ILLUSTRATION = [
    ("green-tilleul-verveine", "Tilleul verveine"),
    ("green-bourgeon", "Bourgeon"),
    ("green-emeraude", "Émeraude"),
    ("green-menthe", "Menthe"),
    ("green-archipel", "Archipel"),
    ("blue-ecume", "Écume"),
    ("blue-cumulus", "Cumulus"),
    ("purple-glycine", "Glycine"),
    ("pink-macaron", "Macaron"),
    ("pink-tuile", "Tuile"),
    ("yellow-tournesol", "Tournesol"),
    ("yellow-moutarde", "Moutarde"),
    ("orange-terre-battue", "Terre battue"),
    ("brown-cafe-creme", "Café crème"),
    ("brown-caramel", "Caramel"),
    ("brown-opera", "Opéra"),
    ("beige-gris-galet", "Gris galet"),
]

COLOR_CHOICES = [
    (_("Primary colors"), COLOR_CHOICES_PRIMARY),
    (_("Neutral colors"), COLOR_CHOICES_NEUTRAL),
    (_("Illustration colors"), COLOR_CHOICES_ILLUSTRATION),
]

COLOR_CHOICES_WITH_SYSTEM = [
    (_("Primary colors"), COLOR_CHOICES_PRIMARY),
    (_("Neutral colors"), COLOR_CHOICES_NEUTRAL),
    (_("System colors"), COLOR_CHOICES_SYSTEM),
    (_("Illustration colors"), COLOR_CHOICES_ILLUSTRATION),
]
