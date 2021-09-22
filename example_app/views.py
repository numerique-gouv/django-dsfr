from django.core.paginator import Paginator
from django.shortcuts import render
from django.views.decorators.http import require_safe

from dsfr.templatetags import dsfr_tags


def init_payload(page_title: str):
    # Returns the common payload passed to most pages:
    # title: the page title
    # breadcrumb_data: a dictionary used by the page's breadcrumb
    # context: a dictionary used for content for the base template

    breadcrumb_data = {"current": page_title, "links": []}

    return {"title": page_title, "breadcrumb_data": breadcrumb_data}


@require_safe
def index(request):
    return render(request, "example_app/index.html")


@require_safe
def page_tag(request, tag_name):
    tag_specifics = {
        "accordion": {
            "title": "Accordéon (accordion)",
            "sample_data": {
                "id": "sample-accordion",
                "title": "Title of the accordion item",
                "content": "<p><b>Bold</b> and <em>emphatic</em> Example content</p>",
            },
            "doc_url": "https://gouvfr.atlassian.net/wiki/spaces/DB/pages/312082509/Accord+on+-+Accordion",
        },
        "accordion_group": {
            "title": "Groupe d’accordéons",
            "sample_data": [
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
            ],
        },
        "alert": {
            "title": "Alertes (alerts)",
            "sample_data": {
                "title": "Title of the accordion item",
                "type": "success",
                "content": "Content of the accordion item (can include html)",
                "heading_tag": "h3",
                "is_collapsible": True,
                "id": "alert-sample-tag",
            },
            "doc_url": "https://gouvfr.atlassian.net/wiki/spaces/DB/pages/736362500/Alertes+-+Alerts",
        },
        "breadcrumb": {"title": "Fil d’Ariane (breadcrumb)"},
        "button": {
            "title": "Boutons (buttons)",
            "sample_data": {
                "label": "Label of the button item",
                "onclick": "alert('button doing stuff')",
            },
            "doc_url": "https://gouvfr.atlassian.net/wiki/spaces/DB/pages/217284660/Boutons+-+Buttons",
        },
        "callout": {
            "title": "Mise en avant (callout)",
            "sample_data": {
                "text": "Text of the callout item",
                "title": "(Optional) Title of the callout item",
                "icon_class": " (Optional) Name of the icon class",
                "button": {  # Optional
                    "onclick": "alert('button being a button')",
                    "label": "button label",
                    "extra_classes": "fr-btn--secondary",
                },
            },
            "doc_url": "https://gouvfr.atlassian.net/wiki/spaces/DB/pages/222331196/Mise+en+avant+-+Call-out",
        },
        "card": {
            "title": "Carte (card)",
            "sample_data": {
                "detail": "Appears before the title of the card item",
                "title": "Title of the card item",
                "description": "Text of the card item",
                "link": "https://www.systeme-de-design.gouv.fr/",
                "image_url": "https://via.placeholder.com/350x200",
            },
            "doc_url": "https://gouvfr.atlassian.net/wiki/spaces/DB/pages/222331445/Carte+-+Card",
        },
        "css": {"title": "CSS global"},
        "favicon": {"title": "Icône de favoris (favicon)"},
        "highlight": {
            "title": "Mise en exergue (highlight)",
            "sample_data": {
                "content": "Content of the highlight item (can include html)",
                "title": "Title of the highlight item",
                "heading_tag": "h4",
                "size_class": "fr-text--sm",
            },
            "doc_url": "https://gouvfr.atlassian.net/wiki/spaces/DB/pages/223019199/Mise+en+exergue+-+Highlight",
        },
        "input": {
            "title": "Champs de saisie (input)",
            "sample_data": {
                "id": "The html id of the input item",
                "label": "Label of the input item",
                "type": "Type of the input item (default: 'text')",
                "onchange": "(Optional) Action that happens when the input is changed",
                "value": "(Optional) Value of the input item",
                "min": "(Optional) Minimum value of the input item (for type='date')",
                "max": "(Optional) Maximum value of the input item (for type='date')",
            },
            "doc_url": "https://gouvfr.atlassian.net/wiki/spaces/DB/pages/217088099/Champs+de+saisie+-+Input",
        },
        "js": {"title": "JS global"},
        "link": {
            "title": "Lien (link)",
            "sample_data": {
                "url": "http://example.com",
                "label": "Label of the link item",
                "is_external": True,
                "extra_classes": "fr-link--lg",
            },
            "doc_url": "https://gouvfr.atlassian.net/wiki/spaces/DB/pages/217284725/Liens+-+Links",
        },
        "pagination": {
            "title": "Pagination (pagination)",
            "doc_url": "https://gouvfr.atlassian.net/wiki/spaces/DB/pages/223051980/Pagination+-+Pagination",
        },
        "select": {
            "title": "Listes déroulantes (selects)",
            "sample_data": {
                "id": "The html id of the select item",
                "label": "Label of the select item",
                "onchange": "(Optional) Action that happens when the select is changed",
                "selected": "(Optional) If the item is selected",
                "default": {  # Optional
                    "disabled": "If the item is disabled",
                    "hidden": "If the item is hidden",
                },
                "options": [
                    {"text": "Option 1", "value": 1},
                    {"text": "Option 2", "value": 2},
                ],
            },
            "doc_url": "https://gouvfr.atlassian.net/wiki/spaces/DB/pages/223019306/Liste+d+roulante+-+Select",
        },
        "summary": {
            "title": "Sommaire (summary)",
            "sample_data": [
                {"link": "link 1", "title": "First item title"},
                {"link": "link 2", "title": "Second item title"},
            ],
            "doc_url": "https://gouvfr.atlassian.net/wiki/spaces/DB/pages/262898307/Sommaire+-+Summary",
        },
        "table": {
            "title": "Tableau (table)",
            "sample_data": {
                "header": ["Colonne 1", "Colonne 2", "Colonne 3"],
                "content": [["a", "b", "c"], ["d", "e", "f"]],
            },
            "doc_url": "https://gouvfr.atlassian.net/wiki/spaces/DB/pages/312016971/Tableau+-+Table",
        },
        "theme_modale": {"title": "Modale de sélection du thème"},
        "tile": {
            "title": "Tuile (tile)",
            "sample_data": {
                "title": "Title of the tile item",
                "url": "URL of the link of the tile item",
                "image_path": "https://via.placeholder.com/90C",
            },
        },
    }

    if tag_name in tag_specifics:
        current_tag = tag_specifics[tag_name]
        payload = init_payload(current_tag["title"])
        payload["tag_name"] = tag_name

        if tag_name == "pagination":
            sample_content = list(range(0, 100))
            paginator = Paginator(sample_content, 10)
            payload["page_obj"] = paginator.get_page(4)

        module = getattr(globals()["dsfr_tags"], f"dsfr_{tag_name}")
        payload["tag_comment"] = module.__doc__

        if "sample_data" in current_tag:
            payload["sample_data"] = current_tag["sample_data"]

        if "doc_url" in current_tag:
            payload["doc_url"] = current_tag["doc_url"]

        return render(request, f"example_app/page_tag.html", payload)
    else:
        payload = init_payload("Non implémenté")
        payload["not_yet"] = {
            "text": "Le contenu recherché n'est pas encore implémenté",
            "title": "Non implémenté",
        }
        return render(request, f"example_app/not_yet.html", payload)


@require_safe
def page_tests(request):
    payload = {}
    callout_1 = {
        "text": "This callout item has a normal button",
        "title": "Callout with actionable button",
        "icon_class": "fr-fi-alert-line",
        "button": {
            "onclick": "alert('button being a button')",
            "label": "button label",
            "extra_classes": "fr-btn--secondary",
        },
    }

    callout_2 = {
        "text": "This callout item has a call-to-action link",
        "title": "Callout with call to action link",
        "icon_class": "fr-fi-external-link-line",
        "button": {
            "label": "button label",
            "url": "https://www.systeme-de-design.gouv.fr/",
            "extra_classes": "fr-btn--secondary",
        },
    }
    payload["callout_1"] = callout_1
    payload["callout_2"] = callout_2
    return render(request, "example_app/tests.html", payload)
