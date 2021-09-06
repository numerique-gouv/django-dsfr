from django import template
from django.core.paginator import Page
from django.template.context import Context

register = template.Library()
"""
Tags used in the "DSFR" templates.
"""

# Global tags


@register.inclusion_tag("dsfr/global_css.html")
def dsfr_css() -> None:
    """
    Returns the HTML for the CSS header tags for DSFR

    **Tag name**::
        dsfr_css
    **Usage**::
        {% dsfr_css %}
    **Example**::
        {% dsfr_css %}
    """
    return None


@register.inclusion_tag("dsfr/global_js.html")
def dsfr_js() -> None:
    """
    Returns the HTML for the JS body tags for DSFR

    **Tag name**::
        dsfr_js
    **Usage**::
        {% dsfr_js %}
    **Example**::
        {% dsfr_js %}
    """
    return None


@register.inclusion_tag("dsfr/favicon.html")
def dsfr_favicon() -> None:
    """
    Returns the HTML for the CSS header tags for the DSFR "Marianne" Favicon

    **Tag name**::
        dsfr_favicon
    **Usage**::
        {% dsfr_favicon %}
    **Example**::
        {% dsfr_favicon %}
    """
    return None


@register.inclusion_tag("dsfr/theme_modale.html")
def dsfr_theme_modale() -> None:
    """
    Returns the HTML for the theme selection modale for DSFR

    **Tag name**::
        dsfr_theme_modale
    **Usage**::
        {% dsfr_theme_modale %}
    **Example**::
        {% dsfr_theme_modale %}
    """
    return None


# Components


@register.inclusion_tag("dsfr/breadcrumb.html", takes_context=True)
def dsfr_breadcrumb(context: Context, breadcrumb_data: dict = {}) -> dict:
    """
    Returns a breadcrumb item. Takes a dict as parameter, with the following structure:

    breadcrumb_data = {
        "links": [{"url": "first-url", "title": "First title"}, {...}],
        "current": "Current page title"
    }

    If the dict is not passed as a parameter, it extracts it from context.

    **Tag name**::
        dsfr_breadcrumb
    **Usage**::
        {% dsfr_breadcrumb breadcrumb_data %}
    **Example**::
        {% dsfr_breadcrumb my_breadcrumb %}
    """
    if not breadcrumb_data:
        if "breadcrumb_data" in context:
            breadcrumb_data = context["breadcrumb_data"]
        else:
            breadcrumb_data = {}
    return {"breadcrumb_data": breadcrumb_data}


@register.inclusion_tag("dsfr/callout.html")
def dsfr_callout(callout_data: dict) -> dict:
    """
    Returns a callout item. Takes a dict as parameter, with the following structure:

    callout_data = {
        "text": "Text of the callout item",
        "title": "(Optional) Title of the callout item",
        "icon_class": " (Optional) Name of the icon class",
        "button": {                                 # Optional
            "onclick": "button action",
            "label": "button label"
        }
    }

    **Tag name**::
        dsfr_callout
    **Usage**::
        {% dsfr_callout callout_data %}
    **Example**::
        {% dsfr_callout my_callout %}
    """
    return {"callout_data": callout_data}


@register.inclusion_tag("dsfr/card.html")
def dsfr_card(card_data: dict, extra_classes: str = "", new_tab: bool = False) -> dict:
    """
    Returns a card item. Takes the following parameters, with the following structure:

    card_data = {
        "detail": "Appears before the title of the card item",
        "title": "Title of the card item",
        "description": "Text of the card item",
        "image": "(Optional) url of the image"
    }

    extra_classes: (Optional) string with names of extra classes
    new_tab: (Optional) if True, forces links to open in a new tab


    **Tag name**::
        dsfr_card
    **Usage**::
        {% dsfr_card card_data %}
    **Example**::
        {% dsfr_card my_card %}
    """
    return {"card_data": card_data, "extra_classes": extra_classes, "new_tab": new_tab}


@register.inclusion_tag("dsfr/input.html")
def dsfr_input(input_data: dict, extra_classes: str = "", **kwargs) -> dict:
    """
    Returns a input item. Takes the following parameters, with the following structure:

    input_data = {
        "id": "The html id of the input item",
        "label": "Label of the input item",
        "type": "Type of the input item (default: 'text')",
        "onchange": "(Optional) Action that happens when the input is changed",
        "value": "(Optional) Value of the input item",
        "min": "(Optional) Minimum value of the input item (for type='date')",
        "max": "(Optional) Maximum value of the input item (for type='date')",
    }

    extra_classes: (Optional) string with names of extra classes

    It is possible to force any of the input_data keys by passing it as an additional parameter.

    **Tag name**::
        dsfr_input
    **Usage**::
        {% dsfr_input input_data %}
    **Example**::
        {% dsfr_input my_input %}
    """

    authorized_keys = ["id", "label", "type", "onchange", "value", "min", "max"]
    for k in kwargs:
        if k in authorized_keys:
            input_data[k] = kwargs[k]

    return {"input_data": input_data, "extra_classes": extra_classes}


@register.inclusion_tag("dsfr/pagination.html", takes_context=True)
def dsfr_pagination(context: Context, page_obj: Page) -> dict:
    """
    Returns a pagination item. Takes a Django paginator object as parameter
    Cf. https://docs.djangoproject.com/fr/3.2/topics/pagination/

    **Tag name**::
        dsfr_pagination
    **Usage**::
        {% dsfr_pagination page_obj %}
    **Example**::
        {% dsfr_pagination page_obj %}
    """
    return {"request": context["request"], "page_obj": page_obj}


@register.inclusion_tag("dsfr/select.html")
def dsfr_select(select_data: dict, extra_classes: str = "", **kwargs) -> dict:
    """
    Returns a select item. Takes the following parameters, with the following structure:

    select_data = {
        "id": "The html id of the select item",
        "label": "Label of the select item",
        "onchange": "(Optional) Action that happens when the select is changed",
        "selected": "(Optional) If the item is selected",
        "default": { # Optional
            "disabled": "If the item is disabled",
            "hidden": "If the item is hidden",
        },
        "options": [
            {"text": "Option 1", "value": 1 },
            {"text": "Option 2", "value": 2 }
        ]
    }

    extra_classes: (Optional) string with names of extra classes

    It is possible to force any of the input_data keys by passing it as an additional parameter.

    **Tag name**::
        dsfr_select
    **Usage**::
        {% dsfr_select select_data %}
    **Example**::
        {% dsfr_select my_select %}
    """

    authorized_keys = ["id", "label", "onchange", "selected", "default", "options"]

    for k in kwargs:
        if k in authorized_keys:
            select_data[k] = kwargs[k]

    return {"select_data": select_data, "extra_classes": extra_classes}


@register.inclusion_tag("dsfr/summary.html")
def dsfr_summary(items: list) -> dict:
    """
    Returns a summary item. Takes a list as parameter, with the following structure:

    items = [{ "link": "item1", "title": "First item title"}, {...}]

    **Tag name**::
        dsfr_summary
    **Usage**::
        {% dsfr_summary items %}
    **Example**::
        {% dsfr_summary my_items %}
    """
    return {"items": items}


@register.inclusion_tag("dsfr/table.html")
def dsfr_table(
    caption: str, content: list, extra_classes: str = "", header: list = []
) -> dict:
    """
    Returns a table item. Takes the following parameters, with the following structure:

    caption = "The title of the table"
    content: list of rows, each row being a list of cells itself

    extra_classes: (Optional) string with names of extra classes
    header: (Optional) list of cells for the table header

    **Tag name**::
        dsfr_table
    **Usage**::
        {% dsfr_table caption="Title" content=content %}
    **Example**::
        {% dsfr_table caption="Toto" content=my_content %}
    """
    return {
        "caption": caption,
        "content": content,
        "extra_classes": extra_classes,
        "header": header,
    }


@register.inclusion_tag("dsfr/tile.html")
def dsfr_tile(tile_data: dict) -> dict:
    """
    Returns a tile item. Takes a dict as parameter, with the following structure:

    tile_data = {
        "title": "Title of the tile item",
        "url": "URL of the link of the tile item",
        "image_path": "path of the tile image",
        "svg_icon": "Boolean, specifies if the tile image is a SVG"
    }

    **Tag name**::
        dsfr_tile
    **Usage**::
        {% dsfr_tile tile_data %}
    **Example**::
        {% dsfr_tile my_tile %}
    """
    return {"tile_data": tile_data}


# Other tags


@register.simple_tag(takes_context=True)
def url_remplace_params(context: Context, **kwargs):
    """
    Allows to make a link that adds or updates a GET parameter while
    keeping the existing ones.
    Useful for combining filters and pagination.

    Sample use:
    <a href="?{% url_remplace_params page=page_obj.next_page_number %}">Next</a>
    """
    query = context["request"].GET.copy()

    for k in kwargs:
        query[k] = kwargs[k]

    return query.urlencode()
