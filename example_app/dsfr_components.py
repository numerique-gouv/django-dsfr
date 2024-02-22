from django.templatetags.static import static

IMPLEMENTED_COMPONENTS = {
    "accordion": {
        "title": "Accordéon (accordion)",
        "sample_data": [
            {
                "id": "sample-accordion",
                "title": "Title of the accordion item",
                "content": "<p><b>Bold</b> and <em>emphatic</em> Example content</p>",
            }
        ],
        "doc_url": "https://www.systeme-de-design.gouv.fr/elements-d-interface/composants/accordeon",
    },
    "alert": {
        "title": "Alertes (alerts)",
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
        ],
        "doc_url": "https://www.systeme-de-design.gouv.fr/elements-d-interface/composants/alerte",
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
    },
    "breadcrumb": {
        "title": "Fil d’Ariane (breadcrumb)",
        "doc_url": "https://www.systeme-de-design.gouv.fr/elements-d-interface/composants/fil-d-ariane",
    },
    "button": {
        "title": "Boutons (buttons)",
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
        ],
        "doc_url": "https://www.systeme-de-design.gouv.fr/elements-d-interface/composants/bouton",
    },
    "callout": {
        "title": "Mise en avant (callout)",
        "sample_data": [
            {
                "title": "Mise en avant avec bouton normal",
                "text": "This callout item has a normal button",
                "icon_class": "fr-icon-alert-line",
                "button": {
                    "onclick": "alert('button being a button')",
                    "label": "button label",
                    "extra_classes": "fr-btn--secondary",
                },
            },
            {
                "title": "Mise en avant avec lien",
                "text": "This callout item has a call-to-action link",
                "icon_class": "fr-icon-external-link-line",
                "button": {
                    "label": "button label",
                    "url": "https://www.systeme-de-design.gouv.fr/",
                    "extra_classes": "fr-btn--secondary",
                },
            },
        ],
        "doc_url": "https://www.systeme-de-design.gouv.fr/elements-d-interface/composants/mise-en-avant",
    },
    "card": {
        "title": "Carte (card)",
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
                "title": "Carte avec détails d’en-tête (badges)",
                "description": """Texte de la carte.
                    Il peut prendre jusqu’à 200 caractères.
                    """,
                "link": "https://www.systeme-de-design.gouv.fr/",
                "new_tab": True,
                "top_detail": {
                    "detail": {
                        "icon_class": "fr-icon-warning-fill",
                        "text": "Détail (optionnel)",
                    },
                    "badges": [
                        {
                            "label": "Badge 1",
                        },
                        {
                            "label": "Badge 2",
                        },
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
                "title": "Télécharger le fichier",
                "description": """Exemple de carte de téléchargement, avec un texte un peu long, qui peut
                aller jusqu’à 200 caractères.""",
                "link": "https://www.systeme-de-design.gouv.fr/",
                "image_url": "/django-dsfr/static/img/placeholder.1x1.svg",
                "new_tab": True,
                "bottom_detail": {
                    "text": "PNG — 1,1 ko",
                },
                "extra_classes": "fr-card--horizontal fr-card--download",
            },
        ],
        "doc_url": "https://www.systeme-de-design.gouv.fr/elements-d-interface/composants/carte",
    },
    "favicon": {
        "title": "Icône de favoris (favicon)",
        "doc_url": "https://www.systeme-de-design.gouv.fr/elements-d-interface/composants/icones-de-favoris",
    },
    "highlight": {
        "title": "Mise en exergue (highlight)",
        "sample_data": [
            {
                "content": "Content of the highlight item (can include html)",
                "size_class": "fr-text--sm",
            }
        ],
        "doc_url": "https://www.systeme-de-design.gouv.fr/elements-d-interface/composants/mise-en-exergue",
    },
    "input": {
        "title": "Champs de saisie (input)",
        "sample_data": [
            {
                "id": "example-input-id",
                "label": "Label of the input item",
                "type": "text",
                "onchange": "alert(value)",
                "value": "(Optional) Value of the input item",
            },
            {
                "label": "Label of the input item",
                "type": "date",
                "onchange": "alert(value)",
                "value": "2021-09-16",
                "min": "2021-09-04",
                "max": "2021-09-23",
            },
        ],
        "doc_url": "https://www.systeme-de-design.gouv.fr/elements-d-interface/composants/champ-de-saisie",
    },
    "link": {
        "title": "Lien (link)",
        "sample_data": [
            {
                "url": "https://www.systeme-de-design.gouv.fr/",
                "label": "Texte du lien",
                "is_external": True,
                "extra_classes": "fr-link--lg",
            }
        ],
        "doc_url": "https://www.systeme-de-design.gouv.fr/elements-d-interface/composants/liens",
    },
    "pagination": {
        "title": "Pagination (pagination)",
        "doc_url": "https://www.systeme-de-design.gouv.fr/elements-d-interface/composants/pagination",
    },
    "quote": {
        "title": "Citation (quote)",
        "sample_data": [
            {
                "text": "Développer vos sites et applications en utilisant des composants prêts à l’emploi, accessibles et ergonomiques",  # noqa
                "source_url": "https://www.systeme-de-design.gouv.fr/",
                "author": "Auteur",
                "source": "Système de Design de l'État",
                "details": [
                    {"text": "Detail sans lien"},
                    {
                        "text": "Detail avec lien",
                        "link": "https://template.incubateur.net/",
                    },
                ],
                "image_url": "/django-dsfr/static/img/placeholder.1x1.svg",
            }
        ],
        "doc_url": "https://www.systeme-de-design.gouv.fr/elements-d-interface/composants/citation",
    },
    "select": {
        "title": "Listes déroulantes (selects)",
        "sample_data": [
            {
                "id": "select-example-id",
                "label": "Label of the select item",
                "onchange": "console.log(value)",
                "default": {  # Optional
                    "disabled": True,
                    "hidden": True,
                    "text": "Chose an option",
                },
                "options": [
                    {"text": "Option 1", "value": 1},
                    {"text": "Option 2", "value": 2},
                ],
            }
        ],
        "doc_url": "https://www.systeme-de-design.gouv.fr/elements-d-interface/composants/liste-deroulante",
    },
    "sidemenu": {
        "title": "Menu latéral (sidemenu)",
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
                                        "link": "/django-dsfr/tags/sidemenu/",
                                    },
                                ],
                            },
                        ],
                    },
                ],
            }
        ],
        "doc_url": "https://www.systeme-de-design.gouv.fr/elements-d-interface/composants/menu-lateral",
    },
    "skiplinks": {
        "title": "Liens d’évitement (skiplinks)",
        "sample_data": [
            [
                {"link": "#contenu", "label": "Contenu"},
                {"link": "#navigation-header", "label": "Menu"},
            ]
        ],
        "doc_url": "https://www.systeme-de-design.gouv.fr/elements-d-interface/composants/liens-d-evitement",
    },
    "stepper": {
        "title": "Indicateur d’étapes (stepper)",
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
    },
    "summary": {
        "title": "Sommaire (summary)",
        "sample_data": [
            [
                {"link": "link_1", "label": "First item title"},
                {"link": "link_2", "label": "Second item title"},
            ]
        ],
        "doc_url": "https://www.systeme-de-design.gouv.fr/elements-d-interface/composants/sommaire",
    },
    "table": {
        "title": "Tableau (table)",
        "sample_data": [
            {
                "caption": "Titre du tableau",
                "header": ["Colonne 1", "Colonne 2", "Colonne 3"],
                "content": [["a", "b", "c"], ["d", "e", "f"]],
            }
        ],
        "doc_url": "https://www.systeme-de-design.gouv.fr/elements-d-interface/composants/tableau",
    },
    "tag": {
        "title": "Tag (tag)",
        "sample_data": [
            {"label": "Tag simple"},
            {"label": "Tag avec lien", "link": "/django-dsfr/tags"},
            {
                "label": "Petit tag avec icône",
                "extra_classes": "fr-tag--sm fr-icon-arrow-right-line fr-tag--icon-left",  # noqa
            },
            {
                "label": "Tag avec action",
                "link": "#",
                "extra_classes": "fr-icon-close-line fr-tag--icon-right",
                "onclick": "alert('clicked'); return false;",
            },
            {
                "label": "Tag sélectionnable",
                "is_selectable": True,
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
    },
    "theme_modale": {
        "title": "Paramètres d'affichage (display)",
        "doc_url": "https://www.systeme-de-design.gouv.fr/elements-d-interface/composants/parametres-d-affichage",
    },
    "tile": {
        "title": "Tuile (tile)",
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
    },
}

EXTRA_COMPONENTS = {
    "accordion_group": {
        "title": "Groupe d’accordéons (accordion_group)",
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
    },
    "badge_group": {
        "title": "Groupe de badges (badge_group)",
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
    },
    "css": {"title": "CSS global"},
    "js": {"title": "JS global"},
    "form": {"title": "Formulaire"},
    "form_field": {"title": "Formulaire - champ"},
    "django_messages": {
        "title": "Messages Django dans une alerte",
        "sample_data": [{"is_collapsible": True}],
    },
}

unsorted_IMPLEMENTED_COMPONENTS = {**IMPLEMENTED_COMPONENTS, **EXTRA_COMPONENTS}
ALL_IMPLEMENTED_COMPONENTS = dict(sorted(unsorted_IMPLEMENTED_COMPONENTS.items()))

NOT_YET_IMPLEMENTED_COMPONENTS = {
    "file_upload": {
        "title": "Ajout de fichier (file upload)",
        "doc_url": "https://www.systeme-de-design.gouv.fr/elements-d-interface/composants/ajout-de-fichier",
    },
    "notice": {
        "title": "Bandeau d’information importante (notice)",
        "doc_url": "https://www.systeme-de-design.gouv.fr/elements-d-interface/composants/bandeau-d-information-importante",
    },
    "search_bar": {
        "title": "Barre de recherche (search bar)",
        "doc_url": "https://www.systeme-de-design.gouv.fr/elements-d-interface/composants/barre-de-recherche",
    },
    "franceconnect": {
        "title": "Bouton FranceConnect",
        "doc_url": "https://www.systeme-de-design.gouv.fr/elements-d-interface/composants/bouton-franceconnect",
    },
    "radio": {
        "title": "Bouton radio (radio)",
        "doc_url": "https://www.systeme-de-design.gouv.fr/elements-d-interface/composants/boutons-radio",
    },
    "radio_rich": {
        "title": "Bouton radio riche (radio_rich)",
        "doc_url": "https://www.systeme-de-design.gouv.fr/elements-d-interface/composants/boutons-radio-riches",
    },
    "checkbox": {
        "title": "Case à cocher (checkbox)",
        "doc_url": "https://www.systeme-de-design.gouv.fr/elements-d-interface/composants/case-a-cocher",
    },
    "responsive_medias": {
        "title": "Contenu média (responsive_medias)",
        "doc_url": "https://www.systeme-de-design.gouv.fr/elements-d-interface/composants/contenu-medias",
    },
    "segmented_control": {
        "title": "Contrôle segmenté (segmented_control)",
        "doc_url": "https://www.systeme-de-design.gouv.fr/elements-d-interface/composants/controle-segmente",
    },
    "cursor": {
        "title": "Curseur (range)",
        "doc_url": "https://www.systeme-de-design.gouv.fr/elements-d-interface/composants/curseur-range",
    },
    "consent": {
        "title": "Gestionnaire de consentement (consent)",
        "doc_url": "https://www.systeme-de-design.gouv.fr/elements-d-interface/composants/gestionnaire-de-consentement",
    },
    "tooltip": {
        "title": "Infobulle (tooltip)",
        "doc_url": "https://www.systeme-de-design.gouv.fr/elements-d-interface/composants/infobulle",
    },
    "toggle": {
        "title": "Interrupteur (toggle)",
        "doc_url": "https://www.systeme-de-design.gouv.fr/elements-d-interface/composants/interrupteur",
    },
    "newsletter_follow": {
        "title": "Lettre d’information et réseaux sociaux (newsletter & follow)",
        "doc_url": "https://www.systeme-de-design.gouv.fr/elements-d-interface/composants/lettre-d-info-et-reseaux-sociaux",
    },
    "modal": {
        "title": "Modale (modal)",
        "doc_url": "https://www.systeme-de-design.gouv.fr/elements-d-interface/composants/modale",
    },
    "password": {
        "title": "Mot de passe (password)",
        "doc_url": "https://www.systeme-de-design.gouv.fr/elements-d-interface/composants/mot-de-passe",
    },
    "navigation": {
        "title": "Navigation principale (navigation)",
        "doc_url": "https://www.systeme-de-design.gouv.fr/elements-d-interface/composants/navigation-principale",
    },
    "share": {
        "title": "Partage (share)",
        "doc_url": "https://www.systeme-de-design.gouv.fr/elements-d-interface/composants/partage",
    },
    "back_to_top": {
        "title": "Retour en haut de page (back to top)",
        "doc_url": "https://www.systeme-de-design.gouv.fr/elements-d-interface/composants/retour-en-haut-de-page",
    },
    "translate": {
        "title": "Sélecteur de langue",
        "doc_url": "https://www.systeme-de-design.gouv.fr/elements-d-interface/composants/selecteur-de-langue",
    },
    "download": {
        "title": "Téléchargement de fichier",
        "doc_url": "https://www.systeme-de-design.gouv.fr/elements-d-interface/composants/telechargement-de-fichier",
    },
    "transcription": {
        "title": "Transcription",
        "doc_url": "https://www.systeme-de-design.gouv.fr/elements-d-interface/composants/transcription",
    },
}

# There is no need for specific tags for these
# (either because the DSFR is implemented globally or because they are
# broken down into more specific tags)
WONT_BE_IMPLEMENTED = {
    "core": {"title": "Fondamentaux (core)"},
    "forms": {"title": "Formulaire (forms)"},
    "legacy": {"title": "Systèmes antérieurs (legacy)"},
    "logo": {"title": "Bloc marque (logo)"},
    "utilites": {"title": "Outil (utilities)"},
    "tab": {"title": "Onglet (tab)"},
}

all_tags_unsorted = {
    **IMPLEMENTED_COMPONENTS,
    **EXTRA_COMPONENTS,
    **NOT_YET_IMPLEMENTED_COMPONENTS,
    **WONT_BE_IMPLEMENTED,
}
ALL_TAGS = dict(sorted(all_tags_unsorted.items()))
