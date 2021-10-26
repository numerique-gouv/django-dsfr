IMPLEMENTED_TAGS = {
    "accordion": {
        "title": "Accordéon (accordion)",
        "sample_data": [
            {
                "id": "sample-accordion",
                "title": "Title of the accordion item",
                "content": "<p><b>Bold</b> and <em>emphatic</em> Example content</p>",
            }
        ],
        "doc_url": "https://gouvfr.atlassian.net/wiki/spaces/DB/pages/312082509/Accord+on+-+Accordion",
    },
    "alert": {
        "title": "Alertes (alerts)",
        "sample_data": [
            {
                "title": "Title of the alert item",
                "type": "success",
                "content": "Content of the alert item (can include html)",
                "heading_tag": "h3",
                "is_collapsible": True,
                "id": "alert-success-tag",
            },
            {
                "title": "Title of the alert item",
                "type": "error",
                "content": "Content of the alert item (can include html)",
                "heading_tag": "h3",
                "is_collapsible": True,
            },
            {
                "title": "Title of the alert item",
                "type": "info",
                "content": "Content of the alert item (can include html)",
                "heading_tag": "h3",
            },
        ],
        "doc_url": "https://gouvfr.atlassian.net/wiki/spaces/DB/pages/736362500/Alertes+-+Alerts",
    },
    "breadcrumb": {"title": "Fil d’Ariane (breadcrumb)"},
    "button": {
        "title": "Boutons (buttons)",
        "sample_data": [
            {
                "label": "Label of the button item",
                "onclick": "alert('button doing stuff')",
            }
        ],
        "doc_url": "https://gouvfr.atlassian.net/wiki/spaces/DB/pages/217284660/Boutons+-+Buttons",
    },
    "callout": {
        "title": "Mise en avant (callout)",
        "sample_data": [
            {
                "title": "Mise en avant avec bouton normal",
                "text": "This callout item has a normal button",
                "icon_class": "fr-fi-alert-line",
                "button": {
                    "onclick": "alert('button being a button')",
                    "label": "button label",
                    "extra_classes": "fr-btn--secondary",
                },
            },
            {
                "title": "Mise en avant avec lien",
                "text": "This callout item has a call-to-action link",
                "icon_class": "fr-fi-external-link-line",
                "button": {
                    "label": "button label",
                    "url": "https://www.systeme-de-design.gouv.fr/",
                    "extra_classes": "fr-btn--secondary",
                },
            },
        ],
        "doc_url": "https://gouvfr.atlassian.net/wiki/spaces/DB/pages/222331196/Mise+en+avant+-+Call-out",
    },
    "card": {
        "title": "Carte (card)",
        "sample_data": [
            {
                "detail": "Appears before the title of the card item",
                "title": "Title of the card item",
                "description": "Text of the card item",
                "link": "https://www.systeme-de-design.gouv.fr/",
                "image_url": "https://via.placeholder.com/350x200",
                "new_tab": True,
            }
        ],
        "doc_url": "https://gouvfr.atlassian.net/wiki/spaces/DB/pages/222331445/Carte+-+Card",
    },
    "favicon": {"title": "Icône de favoris (favicon)"},
    "highlight": {
        "title": "Mise en exergue (highlight)",
        "sample_data": [
            {
                "content": "Content of the highlight item (can include html)",
                "size_class": "fr-text--sm",
            }
        ],
        "doc_url": "https://gouvfr.atlassian.net/wiki/spaces/DB/pages/223019199/Mise+en+exergue+-+Highlight",
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
        "doc_url": "https://gouvfr.atlassian.net/wiki/spaces/DB/pages/217088099/Champs+de+saisie+-+Input",
    },
    "link": {
        "title": "Lien (link)",
        "sample_data": [
            {
                "url": "https://www.systeme-de-design.gouv.fr/",
                "label": "Label of the link item",
                "is_external": True,
                "extra_classes": "fr-link--lg",
            }
        ],
        "doc_url": "https://gouvfr.atlassian.net/wiki/spaces/DB/pages/217284725/Liens+-+Links",
    },
    "pagination": {
        "title": "Pagination (pagination)",
        "doc_url": "https://gouvfr.atlassian.net/wiki/spaces/DB/pages/223051980/Pagination+-+Pagination",
    },
    "quote": {
        "title": "Citation (quote)",
        "sample_data": [
            {
                "text": "Développer vos sites et applications en utilisant des composants prêts à l'emploi, accessibles et ergonomiques",
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
                "image_url": "https://via.placeholder.com/150x150",
            }
        ],
        "doc_url": "https://gouvfr.atlassian.net/wiki/spaces/DB/pages/771358744/Citation+-+Quote",
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
                },
                "options": [
                    {"text": "Option 1", "value": 1},
                    {"text": "Option 2", "value": 2},
                ],
            }
        ],
        "doc_url": "https://gouvfr.atlassian.net/wiki/spaces/DB/pages/223019306/Liste+d+roulante+-+Select",
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
                                        "link": "/sidemenu/",
                                    },
                                ],
                            },
                        ],
                    },
                ],
            }
        ],
        "doc_url": "https://gouvfr.atlassian.net/wiki/spaces/DB/pages/258998801/Menu+lat+ral+-+Side+menu",
    },
    "skiplinks": {
        "title": "Liens d’évitement (skiplinks)",
        "sample_data": [
            [
                {"link": "#contenu", "label": "Contenu"},
                {"link": "#navigation-header", "label": "Menu"},
            ]
        ],
        "doc_url": "https://gouvfr.atlassian.net/wiki/spaces/DB/pages/260014417/Liens+d+vitement+-+Skiplinks",
    },
    "summary": {
        "title": "Sommaire (summary)",
        "sample_data": [
            [
                {"link": "link 1", "label": "First item title"},
                {"link": "link 2", "label": "Second item title"},
            ]
        ],
        "doc_url": "https://gouvfr.atlassian.net/wiki/spaces/DB/pages/262898307/Sommaire+-+Summary",
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
        "doc_url": "https://gouvfr.atlassian.net/wiki/spaces/DB/pages/312016971/Tableau+-+Table",
    },
    "tag": {
        "title": "Tag (tag)",
        "sample_data": [
            {"label": "Tag simple"},
            {"label": "Tag avec lien", "link": "/django-dsfr/tags"},
            {
                "label": "Petit tag avec icône",
                "extra_classes": "fr-tag--sm fr-fi-arrow-right-line fr-tag--icon-left",
            },
        ],
        "doc_url": "https://gouvfr.atlassian.net/wiki/spaces/DB/pages/310706305/Tag",
    },
    "theme_modale": {
        "title": "Modale de sélection du thème",
        "doc_url": "https://gouvfr.atlassian.net/wiki/spaces/DB/pages/579928166/Param+tres+d+affichage+-+Switch+theme",
    },
    "tile": {
        "title": "Tuile (tile)",
        "sample_data": [
            {
                "title": "Title of the tile item",
                "url": "URL of the link of the tile item",
                "image_path": "https://via.placeholder.com/90C",
            }
        ],
    },
}

EXTRA_TAGS = {
    "accordion_group": {
        "title": "Groupe d’accordéons (accordion_group)",
        "sample_data": [
            [
                {
                    "id": "sample-accordion-1",
                    "title": "First accordion item",
                    "content": "<p><b>Bold</b> and <em>emphatic</em> Example content (1)</p>",
                },
                {
                    "id": "sample-accordion-2",
                    "title": "Second accordion item",
                    "content": "<p><b>Bold</b> and <em>emphatic</em> Example content (2)</p>",
                },
                {
                    "id": "sample-accordion-3",
                    "title": "Third accordion item",
                    "content": "<p><b>Bold</b> and <em>emphatic</em> Example content (3)</p>",
                },
            ]
        ],
    },
    "css": {"title": "CSS global"},
    "js": {"title": "JS global"},
}

unsorted_implemented_tags = {**IMPLEMENTED_TAGS, **EXTRA_TAGS}
ALL_IMPLEMENTED_TAGS = dict(sorted(unsorted_implemented_tags.items()))

NOT_YET_IMPLEMENTED_TAGS = {
    "search": {
        "title": "Barre de recherche (search)",
        "doc_url": "https://gouvfr.atlassian.net/wiki/spaces/DB/pages/217186376/Barre+de+recherche+-+Search+bar",
    },
    "logo": {
        "title": "Bloc marque (logo)",
    },
    "radio": {
        "title": "Bouton radio (radio)",
        "doc_url": "https://gouvfr.atlassian.net/wiki/spaces/DB/pages/217088553/Boutons+radio+-+Radio+button",
    },
    "radio_rich": {
        "title": "Bouton radio riche (radio_rich)",
        "doc_url": "https://gouvfr.atlassian.net/wiki/spaces/DB/pages/368935129/Boutons+radio+riches+-+Radio+buttons+extended",
    },
    "checkbox": {"title": "Case à cocher (checkbox)"},
    "media_content": {"title": "Contenu média (media_content)"},
    "consent": {"title": "Gestionnaire de consentement (consent)"},
    "toggle": {"title": "Interrupteur (toggle)"},
    "follow": {"title": "Lettre d’information et réseaux sociaux (follow)"},
    "modal": {"title": "Modale (modal)"},
    "navigation": {"title": "Navigation principale (navigation)"},
    "tab": {"title": "Onglet (tab)"},
    "share": {"title": "Partage (share)"},
}

# There is no need for specific tags for these
# (either because the DSFR is implemented globally or because they are
# broken down into more specific tags)
WONT_BE_IMPLEMENTED = {
    "core": {"title": "Fondamentaux (core)"},
    "forms": {"title": "Formulaire (forms)"},
    "utilites": {"title": "Outil (utilities)"},
    "legacy": {"title": "Systèmes anterieurs (legacy)"},
}

all_tags_unsorted = {
    **IMPLEMENTED_TAGS,
    **EXTRA_TAGS,
    **NOT_YET_IMPLEMENTED_TAGS,
    **WONT_BE_IMPLEMENTED,
}
ALL_TAGS = dict(sorted(all_tags_unsorted.items()))
