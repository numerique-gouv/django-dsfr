from django.utils.translation import gettext_lazy as _

# List of languages for which the interface translation is currently available
DJANGO_DSFR_LANGUAGES = [
    ("en", _("English")),
    ("fr", _("French")),
]

# Color palettes, per https://www.systeme-de-design.gouv.fr/version-courante/fr/fondamentaux/couleurs--palette

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

# Types allowed for the site Notice
NOTICE_TYPE_CHOICES = [
    (
        _("Generic notices"),
        [
            ("info", _("Information")),
            ("warning", _("Warning")),
            ("alert", _("Alert")),
        ],
    ),
    (
        _("Weather alert notices"),
        [
            ("weather-orange", _("Orange weather alert")),
            ("weather-red", _("Red weather alert")),
            ("weather-purple", _("Purple weather alert")),
        ],
    ),
    (
        _("Alert notices"),
        [
            ("attack", _("Attack alert")),
            ("witness", _("Call for witnesses")),
            ("cyberattack", _("Cyberattack")),
        ],
    ),
]

# Ratio classes used for medias and cards
IMAGE_RATIOS = [
    ("fr-ratio-32x9", "32x9"),
    ("fr-ratio-16x9", "16x9"),
    ("fr-ratio-3x2", "3x2"),
    ("fr-ratio-4x3", "4x3"),
    ("fr-ratio-1x1", "1x1"),
    ("fr-ratio-3x4", "3x4"),
    ("fr-ratio-2x3", "2x3"),
]

VIDEO_RATIOS = [
    ("fr-ratio-16x9", "16x9"),
    ("fr-ratio-4x3", "4x3"),
    ("fr-ratio-1x1", "1x1"),
]
