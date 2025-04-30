from django.templatetags.static import static

from example_app.utils import lorem_ipsum

# Sample SVG file
with open("example_app/static/img/gouvernement.svg") as svg_file:
    gov_svg = svg_file.read()

IMPLEMENTED_COMPONENTS = {
    "accordion": {
        "title": "Accordéon",
        "sample_data": [
            {
                "id": "sample-accordion",
                "title": "Titre de l’objet accordéon",
                "content": "<p>Contenu d’exemple avec du <strong>gras</strong> et de l’<em>italique</em></p>",
            }
        ],
        "doc_url": "https://www.systeme-de-design.gouv.fr/elements-d-interface/composants/accordeon",
        "example_url": "https://main--ds-gouv.netlify.app/example/component/accordion/",
        "storybook_url": "https://storybook.systeme-de-design.gouv.fr/?path=/docs/accordion--docs",
    },
    "alert": {
        "title": "Alertes",
        "sample_data": [
            {
                "title": "Alerte refermable de type succès",
                "type": "success",
                "content": "Cliquer sur la croix pour fermer l’alerte.",
                "heading_tag": "h3",
                "is_collapsible": True,
                "id": "alert-success-tag",
            },
            {
                "title": "Alerte refermable de type erreur",
                "type": "error",
                "content": "Cliquer sur la croix pour fermer l’alerte.",
                "heading_tag": "h3",
                "is_collapsible": True,
            },
            {
                "title": "Alerte non-refermable de type info",
                "type": "info",
                "content": "Cette alerte n’a pas de croix de fermeture.",
                "heading_tag": "h3",
            },
            {
                "type": "warning",
                "heading_tag": "h3",
                "title": "Alerte medium sans contenu",
            },
            {
                "type": "warning",
                "content": "Petite alerte sans titre.",
                "extra_classes": "fr-alert--sm",
            },
        ],
        "doc_url": "https://www.systeme-de-design.gouv.fr/elements-d-interface/composants/alerte",
        "example_url": "https://main--ds-gouv.netlify.app/example/component/alert/",
        "storybook_url": "https://storybook.systeme-de-design.gouv.fr/?path=/docs/alert--docs",
    },
    "badge": {
        "title": "Badge",
        "sample_data": [
            {
                "label": "Badge simple",
                "extra_classes": "",
            },
            {
                "label": "Petit badge",
                "extra_classes": "fr-badge--sm",
            },
            {
                "label": "Badge coloré",
                "extra_classes": "fr-badge--green-menthe",
            },
            {
                "label": "Badge système",
                "extra_classes": "fr-badge--success",
            },
        ],
        "doc_url": "https://www.systeme-de-design.gouv.fr/elements-d-interface/composants/badge",
        "example_url": "https://main--ds-gouv.netlify.app/example/component/badge/",
        "storybook_url": "https://storybook.systeme-de-design.gouv.fr/?path=/docs/badge--docs",
    },
    "breadcrumb": {
        "title": "Fil d’Ariane",
        "doc_url": "https://www.systeme-de-design.gouv.fr/elements-d-interface/composants/fil-d-ariane",
        "example_url": "https://main--ds-gouv.netlify.app/example/component/breadcrumb/",
        "storybook_url": "https://storybook.systeme-de-design.gouv.fr/?path=/docs/breadcrumb--docs",
    },
    "button": {
        "title": "Boutons",
        "sample_data": [
            {
                "label": "Bouton principal",
                "onclick": "alert('Vous avez cliqué sur le bouton principal')",
            },
            {
                "label": "Bouton secondaire",
                "name": "secundary-button",
                "type": "button",
                "extra_classes": "fr-btn--secondary",
                "onclick": "alert('Vous avez cliqué sur le bouton secondaire')",
            },
            {
                "label": "Bouton tertiaire",
                "extra_classes": "fr-btn--tertiary",
                "onclick": "alert('Vous avez cliqué sur le bouton tertiaire')",
            },
            {
                "label": "Bouton tertiaire sans bordure",
                "type": "button",
                "extra_classes": "fr-btn--tertiary-no-outline",
                "onclick": "alert('Vous avez cliqué sur le bouton tertiaire sans bordure')",
            },
        ],
        "doc_url": "https://www.systeme-de-design.gouv.fr/elements-d-interface/composants/bouton",
        "example_url": "https://main--ds-gouv.netlify.app/example/component/button/",
        "storybook_url": "https://storybook.systeme-de-design.gouv.fr/?path=/docs/button--docs",
    },
    "button_group": {
        "title": "Boutons – Groupe",
        "sample_data": [
            {
                "items": [
                    {
                        "label": "Bouton principal",
                        "onclick": "alert('Vous avez cliqué sur le bouton principal')",
                        "extra_classes": "fr-icon-checkbox-circle-line fr-btn--icon-left",
                    },
                    {
                        "label": "Bouton secondaire",
                        "name": "secundary-button",
                        "type": "button",
                        "extra_classes": "fr-icon-checkbox-circle-line fr-btn--icon-left fr-btn--secondary",
                        "onclick": "alert('Vous avez cliqué sur le bouton secondaire')",
                    },
                ],
                "extra_classes": "fr-btns-group--icon-left",
            },
            {
                "items": [
                    {
                        "label": "Bouton principal",
                        "onclick": "alert('Vous avez cliqué sur le bouton principal')",
                    },
                    {
                        "label": "Bouton secondaire",
                        "name": "secundary-button",
                        "type": "button",
                        "extra_classes": "fr-btn--secondary",
                        "onclick": "alert('Vous avez cliqué sur le bouton secondaire')",
                    },
                    {
                        "label": "Bouton tertiaire",
                        "extra_classes": "fr-btn--tertiary",
                        "onclick": "alert('Vous avez cliqué sur le bouton tertiaire')",
                    },
                    {
                        "label": "Bouton tertiaire sans bordure",
                        "type": "button",
                        "extra_classes": "fr-btn--tertiary-no-outline",
                        "onclick": "alert('Vous avez cliqué sur le bouton tertiaire sans bordure')",
                    },
                ],
                "extra_classes": "fr-btns-group--equisized",
            },
            {
                "items": [
                    {
                        "label": "Bouton principal",
                        "onclick": "alert('Vous avez cliqué sur le bouton principal')",
                    },
                    {
                        "label": "Bouton secondaire",
                        "name": "secundary-button",
                        "type": "button",
                        "extra_classes": "fr-btn--secondary",
                        "onclick": "alert('Vous avez cliqué sur le bouton secondaire')",
                    },
                    {
                        "label": "Bouton tertiaire",
                        "extra_classes": "fr-btn--tertiary",
                        "onclick": "alert('Vous avez cliqué sur le bouton tertiaire')",
                    },
                    {
                        "label": "Bouton tertiaire sans bordure",
                        "type": "button",
                        "extra_classes": "fr-btn--tertiary-no-outline",
                        "onclick": "alert('Vous avez cliqué sur le bouton tertiaire sans bordure')",
                    },
                ],
                "extra_classes": "fr-btns-group--inline-sm",
            },
        ],
        "doc_url": "https://www.systeme-de-design.gouv.fr/elements-d-interface/composants/groupe-de-boutons",
        "example_url": "https://main--ds-gouv.netlify.app/example/component/button/",
        "storybook_url": "https://storybook.systeme-de-design.gouv.fr/?path=/docs/buttons-group--docs",
    },
    "callout": {
        "title": "Mise en avant",
        "sample_data": [
            {
                "title": "Mise en avant avec bouton normal",
                "text": "Cette mise en avant a un bouton normal",
                "icon_class": "fr-icon-alert-line",
                "button": {
                    "onclick": "alert('Ce bouton est bien un bouton')",
                    "label": "Bouton normal",
                    "extra_classes": "fr-btn--secondary",
                },
            },
            {
                "title": "Mise en avant avec lien",
                "text": "Cette mise en avant a un lien d’appel à action",
                "icon_class": "fr-icon-external-link-line",
                "button": {
                    "label": "Bouton qui est un lien",
                    "url": "https://www.systeme-de-design.gouv.fr/",
                    "extra_classes": "fr-btn--secondary",
                },
            },
            {
                "title": "Mise en avant en couleur",
                "text": "Cette mise en avant a une classe de couleur",
                "icon_class": "fr-icon-palette-line",
                "extra_classes": "fr-callout--green-emeraude",
            },
        ],
        "doc_url": "https://www.systeme-de-design.gouv.fr/elements-d-interface/composants/mise-en-avant",
        "example_url": "https://main--ds-gouv.netlify.app/example/component/callout/",
        "storybook_url": "https://storybook.systeme-de-design.gouv.fr/?path=/docs/callout--docs",
    },
    "card": {
        "title": "Carte",
        "sample_data": [
            {
                "title": "Carte basique",
                "description": """Texte de la carte.
                    Il peut prendre jusqu’à 200 caractères, ce qui devrait correspondre
                    à environ cinq lignes dans le mode vertical, et deux en horizontal.
                    """,
                "link": "https://www.systeme-de-design.gouv.fr/",
                "image_url": "/django-dsfr/static/img/placeholder.16x9.svg",
                "new_tab": True,
            },
            {
                "title": "Carte horizontale, largeur standard",
                "description": """Texte de la carte.
                    Il peut prendre jusqu’à 200 caractères, ce qui devrait correspondre
                    à environ deux lignes dans le mode horizontal, et cinq en vertical.
                    """,
                "link": "https://www.systeme-de-design.gouv.fr/",
                "image_url": "/django-dsfr/static/img/placeholder.1x1.svg",
                "new_tab": True,
                "extra_classes": "fr-card--horizontal",
            },
            {
                "title": "Carte horizontale, largeur tiers",
                "description": """Texte de la carte.
                    Il peut prendre jusqu’à 200 caractères, ce qui devrait correspondre
                    à environ deux lignes dans le mode horizontal, et cinq en vertical.
                    """,
                "link": "https://www.systeme-de-design.gouv.fr/",
                "image_url": "/django-dsfr/static/img/placeholder.1x1.svg",
                "new_tab": True,
                "extra_classes": "fr-card--horizontal fr-card--horizontal-tier",
            },
            {
                "title": "Carte horizontale, largeur moitié",
                "description": """Texte de la carte.
                    Il peut prendre jusqu’à 200 caractères, ce qui devrait correspondre
                    à environ deux lignes dans le mode horizontal, et cinq en vertical.
                    """,
                "link": "https://www.systeme-de-design.gouv.fr/",
                "image_url": "/django-dsfr/static/img/placeholder.1x1.svg",
                "new_tab": True,
                "extra_classes": "fr-card--horizontal fr-card--horizontal-half",
            },
            {
                "title": "Carte avec badge",
                "description": """Texte de la carte.
                    Il peut prendre jusqu’à 200 caractères.
                    """,
                "link": "https://www.systeme-de-design.gouv.fr/",
                "image_url": "/django-dsfr/static/img/placeholder.1x1.svg",
                "new_tab": True,
                "media_badges": [
                    {
                        "label": "Nouveau",
                        "extra_classes": "fr-badge--new",
                    }
                ],
            },
            {
                "title": "Carte avec détails d’en-tête (tags)",
                "description": """Texte de la carte.
                    Il peut prendre jusqu’à 200 caractères.
                    """,
                "link": "https://www.systeme-de-design.gouv.fr/",
                "new_tab": True,
                "top_detail": {
                    "detail": {
                        "icon_class": "fr-icon-warning-fill",
                        "text": "Détail (optionnel) avec icône (optionnelle)",
                    },
                    "tags": [{"label": "tag 1"}, {"label": "tag 2"}],
                },
            },
            {
                "title": "Carte avec image, ratio, et détails d’en-tête (badges)",
                "description": """Texte de la carte.
                    Il peut prendre jusqu’à 200 caractères.
                    """,
                "link": "https://www.systeme-de-design.gouv.fr/",
                "new_tab": True,
                "image_url": "/django-dsfr/static/img/placeholder.16x9.svg",
                "ratio_class": "fr-ratio-1x1",
                "top_detail": {
                    "detail": {
                        "icon_class": "fr-icon-warning-fill",
                        "text": "Détail (optionnel)",
                    },
                    "badges": [
                        {"label": "Badge 1"},
                        {"extra_classes": "fr-badge--warning", "label": "Badge 2"},
                    ],
                },
            },
            {
                "title": "Carte avec détails en pied",
                "description": """Texte de la carte.
                    Il peut prendre jusqu’à 200 caractères.
                    """,
                "link": "https://www.systeme-de-design.gouv.fr/",
                "new_tab": True,
                "bottom_detail": {
                    "icon": "fr-icon-warning-fill",
                    "text": "Détail (optionnel)",
                },
            },
            {
                "title": "Carte horizontale avec zone d’action (boutons)",
                "description": """Texte de la carte.
                    Il peut prendre jusqu’à 200 caractères.
                    """,
                "link": "https://www.systeme-de-design.gouv.fr/",
                "image_url": "/django-dsfr/static/img/placeholder.1x1.svg",
                "new_tab": True,
                "enlarge_link": False,
                "extra_classes": "fr-card--horizontal",
                "call_to_action": {
                    "buttons": [
                        {"label": "Bouton 1", "extra_classes": "fr-btn--secondary"},
                        {"label": "Bouton 2"},
                    ]
                },
            },
            {
                "title": "Carte horizontale avec zone d’action (liens)",
                "description": """Texte de la carte.
                    Il peut prendre jusqu’à 200 caractères.
                    """,
                "link": "https://www.systeme-de-design.gouv.fr/",
                "image_url": "/django-dsfr/static/img/placeholder.1x1.svg",
                "new_tab": True,
                "enlarge_link": False,
                "extra_classes": "fr-card--horizontal",
                "call_to_action": {
                    "links": [
                        {
                            "url": "/",
                            "label": "Lien interne",
                        },
                        {
                            "url": "https://www.systeme-de-design.gouv.fr/",
                            "label": "Lien externe",
                            "is_external": True,
                        },
                    ]
                },
            },
            {
                "title": "Carte avec un fond gris et une ombre",
                "description": """Texte de la carte.
                    Il peut prendre jusqu’à 200 caractères, ce qui devrait correspondre
                    à environ cinq lignes dans le mode vertical, et deux en horizontal.
                    """,
                "link": "https://www.systeme-de-design.gouv.fr/",
                "image_url": "/django-dsfr/static/img/placeholder.16x9.svg",
                "new_tab": True,
                "extra_classes": "fr-card--grey fr-card--shadow",
            },
            {
                "title": "Carte sans lien",
                "description": """Peut être utile au besoin.""",
                "image_url": "/django-dsfr/static/img/placeholder.1x1.svg",
                "enlarge_link": False,
                "extra_classes": "fr-card--horizontal",
            },
        ],
        "doc_url": "https://www.systeme-de-design.gouv.fr/elements-d-interface/composants/carte",
        "example_url": "https://main--ds-gouv.netlify.app/example/component/card/",
        "storybook_url": "https://storybook.systeme-de-design.gouv.fr/?path=/docs/card--docs",
    },
    "consent": {
        "title": "Gestionnaire de consentement",
        "doc_url": "https://www.systeme-de-design.gouv.fr/elements-d-interface/composants/gestionnaire-de-consentement",
        "example_url": "https://main--ds-gouv.netlify.app/example/component/consent/",
        "storybook_url": "https://storybook.systeme-de-design.gouv.fr/?path=/docs/consent--docs",
        "sample_data": [
            {
                "title": "À propos des cookies sur Django-DSFR",
                "content": """
                Bienvenue ! Nous utilisons des cookies pour améliorer votre expérience et les
                services disponibles sur ce site. Pour en savoir plus, visitez la page <a href="#">
                Données personnelles et cookies</a>. Vous pouvez, à tout moment, avoir le contrôle
                sur les cookies que vous souhaitez activer.
                """,
            }
        ],
    },
    "content": {
        "title": "Contenu média",
        "doc_url": "https://www.systeme-de-design.gouv.fr/elements-d-interface/composants/contenu-medias",
        "example_url": "https://main--ds-gouv.netlify.app/example/component/content/",
        "storybook_url": "https://storybook.systeme-de-design.gouv.fr/?path=/docs/content--docs",
        "sample_data": [
            {
                "image_url": "/django-dsfr/static/img/placeholder.16x9.svg",
                "caption": "Image en largeur normale et en 16x9",
                "alt_text": "Silhouette stylisée représentant le soleil au-dessus de deux montagnes.",
                "ratio_class": "fr-ratio-16x9",
            },
            {
                "image_url": "/django-dsfr/static/img/placeholder.16x9.svg",
                "caption": "Image en largeur normale et en 4x3",
                "alt_text": "Silhouette stylisée représentant le soleil au-dessus de deux montagnes.",
                "ratio_class": "fr-ratio-4x3",
            },
            {
                "image_url": "/django-dsfr/static/img/placeholder.16x9.svg",
                "caption": "Image plus large que la colonne de contenu",
                "alt_text": "Silhouette stylisée représentant le soleil au-dessus de deux montagnes.",
                "extra_classes": "fr-content-media--lg",
            },
            {
                "svg": gov_svg,
                "caption": """Image SVG avec un lien dans la légende.
                                <a class="fr-link" href="https://main--ds-gouv.netlify.app/example/component/content/"
                                    rel="noopener external"
                                    title="Source - Ouvre une nouvelle fenêtre" target="_blank">Source</a>.""",
                "alt_text": "Silhouette stylisée représentant le soleil au-dessus de deux montagnes.",
            },
            {
                "iframe": {
                    "title": "Présentation du portail tubes",
                    "width": "894",
                    "height": "450",
                    "url": "https://tube-numerique-educatif.apps.education.fr/videos/embed/9d0b132d-f836-459a-9b9b-97b1a647232d",
                    "sandbox": "allow-same-origin allow-scripts allow-popups",
                },
                "ratio_class": "fr-ratio-4x3",
                "caption": "Vidéo avec transcription",
                "alt_text": "",
                "transcription": {"content": f"<div>{lorem_ipsum}</div>"},
            },
        ],
    },
    "favicon": {
        "title": "Icône de favoris",
        "doc_url": "https://www.systeme-de-design.gouv.fr/elements-d-interface/composants/icones-de-favoris",
        "example_url": "https://main--ds-gouv.netlify.app/example/core/favicon/",
    },
    "follow": {
        "title": "Lettre d’information et réseaux sociaux",
        "doc_url": "https://www.systeme-de-design.gouv.fr/elements-d-interface/composants/lettre-d-information-et-reseaux-sociaux",
        "example_url": "https://main--ds-gouv.netlify.app/example/component/follow/",
        "storybook_url": "https://storybook.systeme-de-design.gouv.fr/?path=/docs/follow--docs",
    },
    "footer": {
        "title": "Pied de page",
        "storybook_url": "https://storybook.systeme-de-design.gouv.fr/?path=/docs/footer--docs",
    },
    "france_connect": {
        "title": "Bouton FranceConnect",
        "doc_url": "https://www.systeme-de-design.gouv.fr/elements-d-interface/composants/bouton-franceconnect",
        "example_url": "https://main--ds-gouv.netlify.app/example/component/connect/",
        "storybook_url": "https://storybook.systeme-de-design.gouv.fr/?path=/docs/connect--docs",
        "sample_data": [
            {},
            {"id": "france-connect-plus", "plus": True},
        ],
    },
    "header": {
        "title": "En-tête",
        "storybook_url": "https://storybook.systeme-de-design.gouv.fr/?path=/docs/header--docs",
    },
    "highlight": {
        "title": "Mise en exergue",
        "sample_data": [
            {
                "content": "Contenu de la mise en exergue",
                "size_class": "fr-text--sm",
            },
            {
                "content": "Mise en exergue avec bordure colorée",
                "extra_classes": "fr-highlight--green-emeraude",
            },
        ],
        "doc_url": "https://www.systeme-de-design.gouv.fr/elements-d-interface/composants/mise-en-exergue",
        "example_url": "https://main--ds-gouv.netlify.app/example/component/highlight/",
        "storybook_url": "https://storybook.systeme-de-design.gouv.fr/?path=/docs/highlight--docs",
    },
    "input": {
        "title": "Champs de saisie",
        "sample_data": [
            {
                "id": "example-input-id",
                "label": "Label du champ de saisie",
                "type": "text",
                "onchange": "alert(value)",
                "value": "(Optionnel) valeur du champ de saisie",
            },
            {
                "label": "Champ de saisie de date",
                "type": "date",
                "onchange": "alert(value)",
                "value": "2021-09-16",
                "min": "2021-09-04",
                "max": "2021-09-23",
            },
        ],
        "doc_url": "https://www.systeme-de-design.gouv.fr/elements-d-interface/composants/champ-de-saisie",
        "example_url": "https://main--ds-gouv.netlify.app/example/component/input/",
        "storybook_url": "https://storybook.systeme-de-design.gouv.fr/?path=/docs/input--docs",
    },
    "link": {
        "title": "Lien",
        "sample_data": [
            {
                "url": "/django-dsfr/components/link/",
                "label": "Lien interne",
            },
            {
                "url": "https://www.systeme-de-design.gouv.fr/",
                "label": "Lien externe, large",
                "is_external": True,
                "extra_classes": "fr-link--lg",
            },
            {
                "url": "/django-dsfr/components/link/",
                "label": "Petit lien interne avec flèche",
                "is_external": False,
                "extra_classes": "fr-icon-arrow-right-line fr-link--icon-right fr-link--sm",
            },
            {
                "url": "/django-dsfr/components/link/",
                "label": "Lien de téléchargement",
                "extra_classes": "fr-link--download",
            },
        ],
        "doc_url": "https://www.systeme-de-design.gouv.fr/elements-d-interface/composants/lien",
        "example_url": "https://main--ds-gouv.netlify.app/example/component/link/",
        "storybook_url": "https://storybook.systeme-de-design.gouv.fr/?path=/docs/link--docs",
    },
    "notice": {
        "title": "Bandeau d’information importante",
        "doc_url": "https://www.systeme-de-design.gouv.fr/elements-d-interface/composants/bandeau-d-information-importante",
        "example_url": "https://main--ds-gouv.netlify.app/example/component/notice/",
        "storybook_url": "https://storybook.systeme-de-design.gouv.fr/?path=/docs/notice--docs",
        "sample_data": [
            {
                "title": """Bandeau d’information importante par défaut, comprenant dans le titre un texte assez long
                            pour être sur deux lignes, et <a href='#'
                            rel='noopener external'
                            title="intitulé - Ouvre une nouvelle fenêtre" target='_blank'>
                            un lien au fil du texte</a>, sans croix de fermeture.""",
                "is_collapsible": False,
            },
            {
                "title": "Bandeau d’information importante de niveau warning.",
                "description": """Il comprend en description un texte assez long
                            pour être sur deux lignes, et <a href='#'
                            rel='noopener external'
                            title="intitulé - Ouvre une nouvelle fenêtre" target='_blank'>
                            un lien au fil du texte</a>, avec une croix de fermeture.""",
                "type": "warning",
                "is_collapsible": True,
            },
            {
                "title": """Bandeau d’information importante de niveau alert, comprenant un texte assez long
                            pour être sur deux lignes, et <a href='#'
                            rel='noopener external'
                            title="intitulé - Ouvre une nouvelle fenêtre" target='_blank'>
                            un lien au fil du texte</a>, avec une croix de fermeture.""",
                "type": "alert",
                "is_collapsible": True,
            },
            {
                "title": "Vigilance météo orange",
                "description": """Attention, l’utilisation de ce type de bandeau est encadrée, cf. documentation.""",
                "link": "https://www.systeme-de-design.gouv.fr/composants-et-modeles/composants/bandeau-d-information-importante/",
                "type": "weather-orange",
                "icon": "fr-icon-windy-fill",
                "is_collapsible": True,
            },
            {
                "title": "Vigilance météo rouge",
                "description": """Attention, l’utilisation de ce type de bandeau est encadrée, cf. documentation.""",
                "link": "https://www.systeme-de-design.gouv.fr/composants-et-modeles/composants/bandeau-d-information-importante/",
                "type": "weather-red",
                "is_collapsible": True,
            },
            {
                "title": "Vigilance météo violette",
                "description": """Attention, l’utilisation de ce type de bandeau est encadrée, cf. documentation.""",
                "link": "https://www.systeme-de-design.gouv.fr/composants-et-modeles/composants/bandeau-d-information-importante/",
                "type": "weather-purple",
                "is_collapsible": True,
            },
            {
                "title": "Attentat en cours",
                "description": """Attention, l’utilisation de ce type de bandeau est encadrée, cf. documentation.""",
                "link": "https://www.systeme-de-design.gouv.fr/composants-et-modeles/composants/bandeau-d-information-importante/",
                "type": "attack",
                "is_collapsible": True,
            },
            {
                "title": "Appel à témoins",
                "description": """Attention, l’utilisation de ce type de bandeau est encadrée, cf. documentation.""",
                "link": "https://www.systeme-de-design.gouv.fr/composants-et-modeles/composants/bandeau-d-information-importante/",
                "type": "witness",
                "is_collapsible": True,
            },
            {
                "title": "Cyber-attaque",
                "description": """Attention, l’utilisation de ce type de bandeau est encadrée, cf. documentation.""",
                "link": "https://www.systeme-de-design.gouv.fr/composants-et-modeles/composants/bandeau-d-information-importante/",
                "type": "cyberattack",
                "is_collapsible": True,
            },
        ],
    },
    "pagination": {
        "title": "Pagination",
        "doc_url": "https://www.systeme-de-design.gouv.fr/elements-d-interface/composants/pagination",
        "example_url": "https://main--ds-gouv.netlify.app/example/component/pagination/",
        "storybook_url": "https://storybook.systeme-de-design.gouv.fr/?path=/docs/pagination--docs",
    },
    "quote": {
        "title": "Citation",
        "sample_data": [
            {
                "text": "Citation très basique, sans aucun des champs optionnels.",
            },
            {
                "text": "Développer vos sites et applications en utilisant des composants prêts à l’emploi, accessibles et ergonomiques",  # noqa
                "source_url": "https://www.systeme-de-design.gouv.fr/",
                "author": "Auteur",
                "source": "Système de Design de l'État",
                "details": [
                    {"text": "Détail sans lien"},
                    {
                        "text": "Détail avec lien",
                        "link": "https://template.incubateur.net/",
                    },
                ],
                "image_url": "/django-dsfr/static/img/placeholder.1x1.svg",
                "extra_classes": "fr-quote--green-emeraude",
            },
        ],
        "doc_url": "https://www.systeme-de-design.gouv.fr/elements-d-interface/composants/citation",
        "example_url": "https://main--ds-gouv.netlify.app/example/component/quote/",
        "storybook_url": "https://storybook.systeme-de-design.gouv.fr/?path=/docs/quote--docs",
    },
    "select": {
        "title": "Listes déroulantes",
        "sample_data": [
            {
                "id": "select-example-id",
                "label": "Label de l’élément select",
                "onchange": "console.log(value)",
                "default": {
                    "disabled": True,
                    "hidden": True,
                    "text": "Choisissez une option",
                },
                "options": [
                    {"text": "Option 1", "value": 1},
                    {"text": "Option 2", "value": 2},
                ],
            }
        ],
        "doc_url": "https://www.systeme-de-design.gouv.fr/elements-d-interface/composants/liste-deroulante",
        "example_url": "https://main--ds-gouv.netlify.app/example/component/select/",
        "storybook_url": "https://storybook.systeme-de-design.gouv.fr/?path=/docs/select--docs",
    },
    "sidemenu": {
        "title": "Menu latéral",
        "sample_data": [
            {
                "title": "Menu",
                "items": [
                    {
                        "label": "Menu replié",
                        "items": [
                            {
                                "label": "Une page",
                                "link": "#",
                            },
                            {
                                "label": "Une autre page",
                                "link": "/sidemenu",
                            },
                        ],
                    },
                    {
                        "label": "Menu ouvert",
                        "items": [
                            {
                                "label": "Sous-menu replié",
                                "items": [
                                    {"label": "Encore une page", "link": "#"},
                                ],
                            },
                            {
                                "label": "Sous-menu ouvert",
                                "items": [
                                    {"label": "Page non active", "link": "#"},
                                    {
                                        "label": "Page active",
                                        "link": "/django-dsfr/components/sidemenu/",
                                    },
                                ],
                            },
                        ],
                    },
                ],
            }
        ],
        "doc_url": "https://www.systeme-de-design.gouv.fr/elements-d-interface/composants/menu-lateral",
        "example_url": "https://main--ds-gouv.netlify.app/example/component/sidemenu/",
        "storybook_url": "https://storybook.systeme-de-design.gouv.fr/?path=/docs/sidemenu--docs",
    },
    "skiplinks": {
        "title": "Liens d’évitement",
        "sample_data": [
            [
                {"link": "#contenu", "label": "Contenu"},
                {"link": "#navigation-header", "label": "Menu"},
            ]
        ],
        "doc_url": "https://www.systeme-de-design.gouv.fr/elements-d-interface/composants/lien-d-evitement",
        "example_url": "https://main--ds-gouv.netlify.app/example/component/skiplink/",
        "storybook_url": "https://storybook.systeme-de-design.gouv.fr/?path=/docs/skiplink--docs",
    },
    "stepper": {
        "title": "Indicateur d’étapes",
        "sample_data": [
            {
                "current_step_id": "1",
                "current_step_title": "Titre de l’étape en cours",
                "next_step_title": "Titre de la prochaine étape",
                "total_steps": "3",
            },
            {
                "current_step_id": "4",
                "current_step_title": "Titre de la dernière étape",
                "total_steps": "4",
            },
        ],
        "doc_url": "https://www.systeme-de-design.gouv.fr/elements-d-interface/composants/indicateur-d-etapes",
        "example_url": "https://main--ds-gouv.netlify.app/example/component/stepper/",
        "storybook_url": "https://storybook.systeme-de-design.gouv.fr/?path=/docs/stepper--docs",
    },
    "summary": {
        "title": "Sommaire",
        "sample_data": [
            [
                {"link": "#", "label": "Titre du premier élément"},
                {"link": "#", "label": "Titre du second élément"},
            ],
            [
                {"link": "#", "label": "Titre du premier élément"},
                {
                    "link": "#",
                    "label": "Titre du second élément",
                    "children": [
                        {
                            "link": "#",
                            "label": "Titre du premier élément imbriqué",
                        },
                        {
                            "link": "#",
                            "label": "Titre du second élément imbriqué",
                            "children": [
                                {
                                    "link": "#",
                                    "label": "Titre du premier élément imbriqué (niveau inférieur)",
                                },
                                {
                                    "link": "#",
                                    "label": "Titre du second élément imbriqué (niveau inférieur)",
                                },
                            ],
                        },
                    ],
                },
            ],
        ],
        "doc_url": "https://www.systeme-de-design.gouv.fr/elements-d-interface/composants/sommaire",
        "example_url": "https://main--ds-gouv.netlify.app/example/component/summary/",
        "storybook_url": "https://storybook.systeme-de-design.gouv.fr/?path=/docs/summary--docs",
    },
    "table": {
        "title": "Tableau",
        "sample_data": [
            {
                "caption": "Tableau basique",
                "header": ["Colonne 1", "Colonne 2", "Colonne 3"],
                "content": [["a", "b", "c"], ["d", "e", "f"]],
                "extra_classes": "fr-table--sm",
            },
            {
                "caption": "Tableau avec bordure",
                "header": [
                    "Colonne 1",
                    "Colonne 2",
                    "Colonne 3",
                    "Colonne 4",
                    "Colonne 5",
                    "Colonne 6",
                ],
                "content": [
                    [
                        "Lorem ipsum dolor sit amet",
                        "consectetur adipiscing elit",
                        "sed do eiusmod tempor incididunt ut",
                        "labore et dolore magna aliqua",
                        "At quis risus sed vulputate odio ut enim",
                        100.0,
                    ],
                    [
                        "At risus viverra",
                        "adipiscing at in tellus",
                        "integer feugiat",
                        "Aliquam purus sit amet luctus venenatis lectus",
                        "Pellentesque id nibh tortor id aliquet lectus proin",
                        2,
                    ],
                ],
                "extra_classes": "fr-table--bordered",
            },
            {
                "caption": "Tableau non-scrollable",
                "header": [
                    "Colonne 1",
                    "Colonne 2",
                    "Colonne 3",
                    "Colonne 4",
                    "Colonne 5",
                    "Colonne 6",
                ],
                "content": [
                    [
                        "Lorem ipsum dolor sit amet",
                        "consectetur adipiscing elit",
                        "sed do eiusmod tempor incididunt ut",
                        "labore et dolore magna aliqua",
                        "At quis risus sed vulputate odio ut enim",
                        100.0,
                    ],
                    [
                        "At risus viverra",
                        "adipiscing at in tellus",
                        "integer feugiat",
                        "Aliquam purus sit amet luctus venenatis lectus",
                        "Pellentesque id nibh tortor id aliquet lectus proin",
                        2,
                    ],
                ],
                "extra_classes": "fr-table--no-scroll fr-table--bordered",
            },
        ],
        "doc_url": "https://www.systeme-de-design.gouv.fr/elements-d-interface/composants/tableau",
        "example_url": "https://main--ds-gouv.netlify.app/example/component/table/",
        "storybook_url": "https://storybook.systeme-de-design.gouv.fr/?path=/docs/table--docs",
    },
    "tag": {
        "title": "Tag",
        "sample_data": [
            {"label": "Tag simple"},
            {"label": "Tag avec lien", "link": "/django-dsfr/components"},
            {
                "label": "Petit tag avec icône",
                "extra_classes": "fr-tag--sm fr-icon-arrow-right-line fr-tag--icon-left",  # noqa
            },
            {
                "label": "Tag avec action",
                "link": "#",
                "extra_classes": "fr-icon-cursor-line fr-tag--icon-right",
                "onclick": "alert('clicked'); return false;",
            },
            {
                "label": "Tag sélectionnable",
                "is_selectable": True,
            },
            {
                "label": "Tag sélectionné",
                "is_selectable": True,
                "is_selected": True,
            },
            {
                "label": "Tag supprimable",
                "is_dismissable": True,
            },
            {
                "label": "Tag vert",
                "link": "#",
                "extra_classes": "fr-tag--green-emeraude",
            },
        ],
        "doc_url": "https://www.systeme-de-design.gouv.fr/elements-d-interface/composants/tag",
        "example_url": "https://main--ds-gouv.netlify.app/example/component/tag/",
        "storybook_url": "https://storybook.systeme-de-design.gouv.fr/?path=/docs/tag--docs",
    },
    "theme_modale": {
        "title": "Paramètres d’affichage",
        "doc_url": "https://www.systeme-de-design.gouv.fr/elements-d-interface/composants/parametre-d-affichage",
        "example_url": "https://main--ds-gouv.netlify.app/example/component/display/",
        "storybook_url": "https://storybook.systeme-de-design.gouv.fr/?path=/docs/display--docs",
    },
    "tile": {
        "title": "Tuile",
        "sample_data": [
            {
                "title": "Tuile basique (verticale, MD)",
                "url": "/",
                "image_path": static("img/placeholder.1x1.svg"),
            },
            {
                "title": "Tuile horizontale",
                "description": "Tuile horizontale (MD)",
                "detail": "Avec un pictogramme SVG",
                "url": "/",
                "id": "tile-cityhall",
                "extra_classes": "fr-tile--horizontal",
                "svg_path": static(
                    "dsfr/dist/artwork/pictograms/buildings/city-hall.svg"
                ),
            },
            {
                "title": "Tuile verticale (SM)",
                "url": "/",
                "id": "tile-nuclear-plant",
                "extra_classes": "fr-tile--sm",
                "svg_path": static(
                    "dsfr/dist/artwork/pictograms/buildings/nuclear-plant.svg"
                ),
            },
            {
                "title": "Tuile horizontale (SM)",
                "url": "/",
                "id": "tile-map",
                "extra_classes": "fr-tile--horizontal fr-tile--sm",
                "top_detail": {
                    "badges": [
                        {
                            "label": "Badge coloré",
                            "extra_classes": "fr-badge--sm fr-badge--purple-glycine",
                        },
                    ]
                },
                "svg_path": static("dsfr/dist/artwork/pictograms/map/map.svg"),
            },
            {
                "title": "Tuile à fond gris et ombre sans bordure",
                "url": "/",
                "id": "tile-map-noborder",
                "extra_classes": "fr-tile--horizontal fr-tile--grey fr-tile--shadow fr-tile--no-border",
                "svg_path": static("dsfr/dist/artwork/pictograms/leisure/paint.svg"),
            },
            {
                "title": "Tuile de téléchargement",
                "extra_classes": "fr-tile--horizontal fr-tile--download",
                "detail": "PDF — 1,7 Mo",
                "url": "/",
                "svg_path": static(
                    "dsfr/dist/artwork/pictograms/document/document-signature.svg"
                ),
            },
        ],
        "doc_url": "https://www.systeme-de-design.gouv.fr/elements-d-interface/composants/tuile",
        "example_url": "https://main--ds-gouv.netlify.app/example/component/tile/",
        "storybook_url": "https://storybook.systeme-de-design.gouv.fr/?path=/docs/tile--docs",
    },
    "toggle": {
        "title": "Interrupteur",
        "doc_url": "https://www.systeme-de-design.gouv.fr/elements-d-interface/composants/interrupteur",
        "example_url": "https://main--ds-gouv.netlify.app/example/component/toggle/",
        "storybook_url": "https://storybook.systeme-de-design.gouv.fr/?path=/docs/toggle--docs",
        "sample_data": [
            {
                "label": "Interrupteur basique",
            },
            {
                "label": "Interrupteur basique désactivé avec aide",
                "help_text": "Vous ne pouvez pas utiliser cet interrupteur.",
                "is_disabled": True,
            },
            {
                "label": "Interrupteur complet aligné à gauche",
                "help_text": "Cet interrupteur présente toutes les options disponibles",
                "is_disabled": False,
                "extra_classes": "fr-toggle--label-left fr-toggle--border-bottom",
                "id": "toggle-full",
            },
        ],
    },
    "tooltip": {
        "title": "Infobulle",
        "doc_url": "https://www.systeme-de-design.gouv.fr/elements-d-interface/composants/infobulle",
        "example_url": "https://main--ds-gouv.netlify.app/example/component/tooltip/",
        "storybook_url": "https://storybook.systeme-de-design.gouv.fr/?path=/docs/tooltip--docs",
        "sample_data": [
            {
                "content": "Contenu d’une infobule activée au survol",
                "label": "Libellé du lien",
            },
            {
                "content": "Contenu d’une infobule cliquable",
                "is_clickable": True,
                "id": "tooltip-b",
            },
        ],
    },
    "transcription": {
        "title": "Transcription",
        "doc_url": "https://www.systeme-de-design.gouv.fr/elements-d-interface/composants/transcription",
        "example_url": "https://main--ds-gouv.netlify.app/example/component/transcription/",
        "storybook_url": "https://storybook.systeme-de-design.gouv.fr/?path=/docs/transcription--docs",
        "sample_data": [
            {
                "content": "<div><p>Courte transcription basique</p></div>",
            },
            {
                "title": "Transcription très longue",
                "content": f"<div>{lorem_ipsum}</div>",
            },
        ],
    },
}

EXTRA_COMPONENTS = {
    "accordion_group": {
        "title": "Accordéons – Groupe",
        "sample_data": [
            [
                {
                    "id": "sample-accordion-1",
                    "title": "Premier accordéon",
                    "content": "<p>Contenu d’exemple avec du <strong>gras</strong> et de l’<em>italique</em> (1)</p>",  # noqa
                },
                {
                    "id": "sample-accordion-2",
                    "title": "Deuxième accordéon",
                    "content": "<p>Contenu d’exemple avec du <strong>gras</strong> et de l’<em>italique</em> (2)</p>",  # noqa
                },
                {
                    "id": "sample-accordion-3",
                    "title": "Troisième accordéon",
                    "content": "<p>Contenu d’exemple avec du <strong>gras</strong> et de l’<em>italique</em> (3)</p>",  # noqa
                },
            ]
        ],
        "storybook_url": "https://storybook.systeme-de-design.gouv.fr/?path=/docs/accordions-group--docs",
    },
    "badge_group": {
        "title": "Badges – Groupe",
        "sample_data": [
            [
                {
                    "label": "Succès",
                    "extra_classes": "fr-badge--success",
                },
                {
                    "label": "Info",
                    "extra_classes": "fr-badge--info",
                },
                {
                    "label": "Avertissement",
                    "extra_classes": "fr-badge--warning",
                },
                {
                    "label": "Erreur",
                    "extra_classes": "fr-badge--error",
                },
                {
                    "label": "Nouveau",
                    "extra_classes": "fr-badge--new",
                },
            ]
        ],
        "storybook_url": "https://storybook.systeme-de-design.gouv.fr/?path=/docs/badges-group--docs",
    },
    "css": {"title": "CSS global"},
    "js": {"title": "JS global"},
    "form_field": {"title": "Formulaire - champ"},
    "django_messages": {
        "title": "Messages Django dans une alerte",
        "sample_data": [{"is_collapsible": True}],
    },
}

unsorted_IMPLEMENTED_COMPONENTS = {**IMPLEMENTED_COMPONENTS, **EXTRA_COMPONENTS}
ALL_IMPLEMENTED_COMPONENTS = dict(
    sorted(unsorted_IMPLEMENTED_COMPONENTS.items(), key=lambda k: k[1]["title"])
)

NOT_YET_IMPLEMENTED_COMPONENTS = {
    "radio_rich": {
        "title": "Bouton radio riche",
        "doc_url": "https://www.systeme-de-design.gouv.fr/elements-d-interface/composants/bouton-radio-riche",
        "example_url": "https://main--ds-gouv.netlify.app/example/component/radio/",
        "note": """À implémenter au sein des formulaires et non comme une balise.
        cf. [#126](https://github.com/numerique-gouv/django-dsfr/issues/126)
        """,
    },
    "segmented_control": {
        "title": "Contrôle segmenté",
        "doc_url": "https://www.systeme-de-design.gouv.fr/elements-d-interface/composants/controle-segmente",
        "example_url": "https://main--ds-gouv.netlify.app/example/component/segmented/",
        "storybook_url": "https://storybook.systeme-de-design.gouv.fr/?path=/docs/segmented--docs",
        "note": """À implémenter au sein des formulaires et non comme une balise.
        cf. [#128](https://github.com/numerique-gouv/django-dsfr/issues/128)
        """,
    },
    "range": {
        "title": "Curseur",
        "doc_url": "https://www.systeme-de-design.gouv.fr/elements-d-interface/composants/curseur-range",
        "example_url": "https://main--ds-gouv.netlify.app/example/component/range/",
        "storybook_url": "https://storybook.systeme-de-design.gouv.fr/?path=/docs/range--docs",
        "note": """À implémenter au sein des formulaires et non comme une balise.
        cf. [#129](https://github.com/numerique-gouv/django-dsfr/issues/129)
        """,
    },
}

# There is no need for specific tags for these
# (either because the DSFR is implemented globally or because they are
# broken down into more specific tags)
WONT_BE_IMPLEMENTED = {
    "back_to_top": {
        "title": "Retour en haut de page",
        "doc_url": "https://www.systeme-de-design.gouv.fr/elements-d-interface/composants/retour-en-haut-de-page",
        "example_url": "https://main--ds-gouv.netlify.app/example/component/link/back-to-top/",
        "reason": "Utilisez une balise Lien (`dsfr_link`)",
    },
    "checkbox": {
        "title": "Case à cocher",
        "doc_url": "https://www.systeme-de-design.gouv.fr/elements-d-interface/composants/case-a-cocher",
        "example_url": "https://main--ds-gouv.netlify.app/example/component/checkbox/",
        "storybook_url": "https://storybook.systeme-de-design.gouv.fr/?path=/docs/checkbox--docs",
        "reason": "Champ de formulaire.",
    },
    "download": {
        "title": "Téléchargement de fichier",
        "doc_url": "https://www.systeme-de-design.gouv.fr/elements-d-interface/composants/telechargement-de-fichier",
        "example_url": "https://main--ds-gouv.netlify.app/example/component/download/",
        "reason": "Pas un composant mais une série de variantes d’autres composants : [lien](/django-dsfr/components/link/), [carte](/django-dsfr/components/card/), [tuile](/django-dsfr/components/tile/). Voir la documentation de ceux-ci.",
    },
    "file_upload": {
        "title": "Ajout de fichier",
        "doc_url": "https://www.systeme-de-design.gouv.fr/elements-d-interface/composants/ajout-de-fichier",
        "example_url": "https://main--ds-gouv.netlify.app/example/component/upload/",
        "storybook_url": "https://storybook.systeme-de-design.gouv.fr/?path=/docs/upload--docs",
        "reason": "Champ de formulaire.",
    },
    "modal": {
        "title": "Modale",
        "doc_url": "https://www.systeme-de-design.gouv.fr/elements-d-interface/composants/modale",
        "example_url": "https://main--ds-gouv.netlify.app/example/component/modal/",
        "storybook_url": "https://storybook.systeme-de-design.gouv.fr/?path=/docs/modal--docs",
        "reason": "Une balise rendrait l’utilisation plus complexe au lieu de la simplifier.",
    },
    "navigation": {
        "title": "Navigation principale",
        "doc_url": "https://www.systeme-de-design.gouv.fr/elements-d-interface/composants/navigation-principale",
        "example_url": "https://main--ds-gouv.netlify.app/example/component/navigation/",
        "storybook_url": "https://storybook.systeme-de-design.gouv.fr/?path=/docs/navigation--docs",
        "reason": "Partie de l’en-tête, voir la documentation de ce composant.",
    },
    "password": {
        "title": "Mot de passe",
        "doc_url": "https://www.systeme-de-design.gouv.fr/elements-d-interface/composants/mot-de-passe",
        "example_url": "https://main--ds-gouv.netlify.app/example/component/password/",
        "storybook_url": "https://storybook.systeme-de-design.gouv.fr/?path=/docs/password--docs",
        "reason": "Dépendant de l’implémentation des comptes utilisateurs dans le projet Django",
    },
    "radio": {
        "title": "Bouton radio",
        "doc_url": "https://www.systeme-de-design.gouv.fr/elements-d-interface/composants/boutons-radio",
        "example_url": "https://main--ds-gouv.netlify.app/example/component/radio/",
        "storybook_url": "https://storybook.systeme-de-design.gouv.fr/?path=/docs/radio--docs",
        "reason": "Champ de formulaire.",
    },
    "search_bar": {
        "title": "Barre de recherche",
        "doc_url": "https://www.systeme-de-design.gouv.fr/elements-d-interface/composants/barre-de-recherche",
        "example_url": "https://main--ds-gouv.netlify.app/example/component/search/",
        "storybook_url": "https://storybook.systeme-de-design.gouv.fr/?path=/docs/search--docs",
        "reason": "Champ de formulaire.",
    },
    "share": {
        "title": "Partage",
        "doc_url": "https://www.systeme-de-design.gouv.fr/elements-d-interface/composants/partage",
        "example_url": "https://main--ds-gouv.netlify.app/example/component/share/",
        "share": "https://storybook.systeme-de-design.gouv.fr/?path=/docs/share--docs",
        "reason": "Une balise rendrait l’utilisation plus complexe au lieu de la simplifier.",
    },
    "tab": {
        "title": "Onglet",
        "doc_url": "https://www.systeme-de-design.gouv.fr/elements-d-interface/composants/onglet",
        "example_url": "https://main--ds-gouv.netlify.app/example/component/tab/",
        "storybook_url": "https://storybook.systeme-de-design.gouv.fr/?path=/docs/tabs--docs",
        "reason": "Une balise rendrait l’utilisation plus complexe au lieu de la simplifier.",
    },
    "translate": {
        "title": "Sélecteur de langue",
        "doc_url": "https://www.systeme-de-design.gouv.fr/elements-d-interface/composants/selecteur-de-langue",
        "example_url": "https://main--ds-gouv.netlify.app/example/component/translate/",
        "storybook_url": "https://storybook.systeme-de-design.gouv.fr/?path=/docs/translate--docs",
        "reason": "Partie de l’en-tête, voir la documentation de ce composant.",
    },
}

DEPRECATED_COMPONENTS = {
    "form": {
        "title": "Formulaire",
        "since": "2.0.0",
        "reason": "replaced with standard call to {{ form }}.",
    },
}

all_tags_unsorted = {
    **IMPLEMENTED_COMPONENTS,
    **EXTRA_COMPONENTS,
    **NOT_YET_IMPLEMENTED_COMPONENTS,
    **WONT_BE_IMPLEMENTED,
    **DEPRECATED_COMPONENTS,
}
ALL_TAGS = dict(sorted(all_tags_unsorted.items()))
