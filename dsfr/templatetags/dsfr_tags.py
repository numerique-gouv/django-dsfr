from dsfr.utils import (
    find_active_menu_items,
    generate_random_id,
    parse_tag_args,
)
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
    """
    return None


# Components
@register.inclusion_tag("dsfr/accordion.html")
def dsfr_accordion(*args, **kwargs) -> dict:
    """
    Returns an accordion item. Takes a dict as parameter, with the following structure:

    data_dict = {
        "id": "Unique id of the accordion item",
        "title": "Title of the accordion item",
        "content": "Content of the accordion item (can include html)",
        "heading_tag": "(Optional) Heading tag for the accordion title (default: h3)"
    }

    All of the keys of the dict can be passed directly as named parameters of the tag.

    Can be used alone or in a group with the tag dsfr_accordion_group.

    **Tag name**::
        dsfr_accordion
    **Usage**::
        {% dsfr_accordion data_dict %}
    """
    allowed_keys = ["id", "title", "content", "heading_tag"]
    tag_data = parse_tag_args(args, kwargs, allowed_keys)

    if "id" not in tag_data:
        tag_data["id"] = generate_random_id("accordion")

    return {"self": tag_data}


@register.inclusion_tag("dsfr/accordion_group.html")
def dsfr_accordion_group(items: list) -> dict:
    """
    Returns a group of accordion items. Takes a list of dicts as parameters (see the accordeon
    tag for the structure of these dicts.)

    **Tag name**::
        dsfr_accordion_group
    **Usage**::
        {% dsfr_accordion_group data_list %}
    """
    return {"self": {"items": items}}


@register.inclusion_tag("dsfr/alert.html")
def dsfr_alert(*args, **kwargs) -> dict:
    """
    Returns an alert item. Takes a dict as parameter, with the following structure:

    data_dict = {
        "title": "Title of the alert item",
        "type": "Possible values : info, success, error",
        "content": "Content of the accordion item (can include html)",
        "heading_tag": "(Optional) Heading tag for the alert title (default: p)",
        "is_collapsible" : "(Optional) Boolean, set to true to add a 'close' button for the alert (default: false)",
        "id": "Unique id of the alert item (Optional, mandatory if collapsible)",
        "extra_classes": (Optional) string with names of extra classes.
    }

    All of the keys of the dict can be passed directly as named parameters of the tag.

    Relevant extra_classes
    - "fr-alert--sm" : small alert

    **Tag name**::
        dsfr_alert
    **Usage**::
        {% dsfr_alert data_dict %}
    """

    allowed_keys = [
        "id",
        "title",
        "type",
        "content",
        "heading_tag",
        "is_collapsible",
        "extra_classes",
    ]
    tag_data = parse_tag_args(args, kwargs, allowed_keys)

    if "id" not in tag_data:
        tag_data["id"] = generate_random_id("alert")

    if "is_collapsible" not in tag_data:
        tag_data["is_collapsible"] = False
    return {"self": tag_data}


@register.inclusion_tag("dsfr/breadcrumb.html", takes_context=True)
def dsfr_breadcrumb(context: Context, tag_data: dict = {}) -> dict:
    """
    Returns a breadcrumb item. Takes a dict as parameter, with the following structure:

    data_dict = {
        "links": [{"url": "first-url", "title": "First title"}, {...}],
        "current": "Current page title",
        "root_dir": "the root directory, if the site is not installed at the root of the domain"
    }

    If the dict is not passed as a parameter, it extracts it from context.

    **Tag name**::
        dsfr_breadcrumb
    **Usage**::
        {% dsfr_breadcrumb data_dict %}
    """
    if not tag_data:
        if "breadcrumb_data" in context:
            tag_data = context["breadcrumb_data"]
        else:
            tag_data = {}
    return {"self": tag_data}


@register.inclusion_tag("dsfr/button.html")
def dsfr_button(*args, **kwargs) -> dict:
    """
    Returns a button item. Takes a dict as parameter, with the following structure:

    data_dict = {
        "label": "Label of the button item",
        "onclick": "button action",
        "type": "(Optional) type of button (submit or button - default: submit),
        "is_disabled": "(Optional) boolean that indicate if the button is activated (default: False)",
        "extra_classes": "(Optional) string with names of extra classes."
    }

    All of the keys of the dict can be passed directly as named parameters of the tag.

    Relevant extra_classes
    - "fr-btn--secondary" : secundary button
    - "fr-btn--icon-left" and "fr-btn--icon-right": add an icon to the button (associated with an icon class)
    - "fr-btn--sm" and "fr-btn--lg": button smaller or larger than the default size

    **Tag name**::
        dsfr_button
    **Usage**::
        {% dsfr_button data_dict %}
    """
    allowed_keys = [
        "label",
        "onclick",
        "is_disabled",
        "extra_classes",
    ]
    tag_data = parse_tag_args(args, kwargs, allowed_keys)

    for k in kwargs:
        if k in allowed_keys:
            tag_data[k] = kwargs[k]

    if "is_disabled" not in tag_data:
        tag_data["is_disabled"] = False
    return {"self": tag_data}


@register.inclusion_tag("dsfr/callout.html")
def dsfr_callout(*args, **kwargs) -> dict:
    """
    Returns a callout item. Takes a dict as parameter, with the following structure:

    data_dict = {
        "text": "Text of the callout item",
        "title": "(Optional) Title of the callout item",
        "heading_tag": "(Optional) Heading tag for the alert title (default: p)",
        "icon_class": " (Optional) Name of the icon class",
        "button": {                                 # Optional
            "onclick": "button action",
            "label": "button label"
        }
    }

    All of the keys of the dict can be passed directly as named parameters of the tag.

    **Tag name**::
        dsfr_callout
    **Usage**::
        {% dsfr_callout data_dict %}
    """
    allowed_keys = [
        "text",
        "title",
        "heading_tag",
        "icon_class",
        "button",
    ]
    tag_data = parse_tag_args(args, kwargs, allowed_keys)

    return {"self": tag_data}


@register.inclusion_tag("dsfr/card.html")
def dsfr_card(*args, **kwargs) -> dict:
    """
    Returns a card item. Takes a dict as parameter, with the following structure:

    data_dict = {
        "detail": "Appears before the title of the card item",
        "title": "Title of the card item",
        "description": "Text of the card item",
        "image": "(Optional) url of the image",
        "new_tab": "(Optional) if True, forces links to open in a new tab",
        "extra_classes": "(Optional) string with names of extra classes",
    }

    All of the keys of the dict can be passed directly as named parameters of the tag.

    **Tag name**::
        dsfr_card
    **Usage**::
        {% dsfr_card data_dict %}
    """
    allowed_keys = [
        "detail",
        "title",
        "description",
        "image_url",
        "new_tab",
        "extra_classes",
    ]
    tag_data = parse_tag_args(args, kwargs, allowed_keys)

    return {"self": tag_data}


@register.inclusion_tag("dsfr/highlight.html")
def dsfr_highlight(*args, **kwargs) -> dict:
    """
    Returns a highlight item. Takes a dict as parameter, with the following structure:

    data_dict = {
        "content": "Content of the highlight item (can include html)",
        "size_class": "(Optional) string with name of text-size related classes",
    }

    Relevant size_classes:
    - fr-text--sm
    - fr-text--lg

    All of the keys of the dict can be passed directly as named parameters of the tag.

    **Tag name**::
        dsfr_highlight
    **Usage**::
        {% dsfr_highlight data_dict %}
    """

    allowed_keys = [
        "content",
        "size_class",
    ]
    tag_data = parse_tag_args(args, kwargs, allowed_keys)

    return {"self": tag_data}


@register.inclusion_tag("dsfr/input.html")
def dsfr_input(*args, **kwargs) -> dict:
    """
    Returns a input item. Takes a dict as parameter, with the following structure:

    data_dict = {
        "id": "The unique html id of the input item",
        "label": "Label of the input item",
        "type": "Type of the input item (default: 'text')",
        "onchange": "(Optional) Action that happens when the input is changed",
        "value": "(Optional) Value of the input item",
        "min": "(Optional) Minimum value of the input item (for type='date')",
        "max": "(Optional) Maximum value of the input item (for type='date')",
        "extra_classes": "(Optional) string with names of extra classes"
    }


    All of the keys of the dict can be passed directly as named parameters of the tag.

    **Tag name**::
        dsfr_input
    **Usage**::
        {% dsfr_input data_dict %}
    """

    allowed_keys = [
        "id",
        "label",
        "type",
        "onchange",
        "value",
        "min",
        "max",
        "extra_classes",
    ]
    tag_data = parse_tag_args(args, kwargs, allowed_keys)

    if "id" not in tag_data:
        tag_data["id"] = generate_random_id("input")

    return {"self": tag_data}


@register.inclusion_tag("dsfr/link.html")
def dsfr_link(*args, **kwargs) -> dict:
    """
    Returns a link item. Takes a dict as parameter, with the following structure:

    data_dict = {
        "url": "URL of the link item",
        "label": "Label of the link item",
        "is_external": "(Optional) Indicate if the link is external",
        "extra_classes": "(Optional) string with names of extra classes"
    }

    Relevant extra_classes:
        - fr-link--icon-left or fr-link--icon-right with an icon class
        - fr-link--sm for small links
        - fr-link--lg for large links


    All of the keys of the dict can be passed directly as named parameters of the tag.

    **Tag name**::
        dsfr_link
    **Usage**::
        {% dsfr_link data_dict %}
    """

    allowed_keys = [
        "url",
        "label",
        "is_external",
        "extra_classes",
    ]
    tag_data = parse_tag_args(args, kwargs, allowed_keys)

    return {"self": tag_data}


@register.inclusion_tag("dsfr/pagination.html", takes_context=True)
def dsfr_pagination(context: Context, page_obj: Page) -> dict:
    """
    Returns a pagination item. Takes a Django paginator object as parameter
    Cf. https://docs.djangoproject.com/fr/3.2/topics/pagination/

    **Tag name**::
        dsfr_pagination
    **Usage**::
        {% dsfr_pagination page_obj %}
    """
    return {"request": context["request"], "page_obj": page_obj}


@register.inclusion_tag("dsfr/quote.html")
def dsfr_quote(*args, **kwargs) -> dict:
    """
    Returns a quote item. Takes a dict as parameter, with the following structure:

    data_dict = {
        "text": "Text of the quote",
        "source_url": "(Optional) URL of the source of the quote",
        "author": "(Optional) The author of the quote",
        "source": "(Optional) The name of the source of the quote",
        "details": "(Optional) A list containing detail dicts",
        "image_url": "(Optional) URL of an illustrative image",
    }

    The "details" dict entries have a mandatory "text" key and an optional "link" key.

    All of the keys of the dict can be passed directly as named parameters of the tag.

    **Tag name**::
        dsfr_quote
    **Usage**::
        {% dsfr_quote data_dict %}
    """

    allowed_keys = [
        "text",
        "source_url",
        "author",
        "source",
        "details",
        "image_url",
    ]
    tag_data = parse_tag_args(args, kwargs, allowed_keys)

    return {"self": tag_data}


@register.inclusion_tag("dsfr/select.html")
def dsfr_select(*args, **kwargs) -> dict:
    """
    Returns a select item. Takes a dict as parameter, with the following structure:

    data_dict = {
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
        ],
        "extra_classes": "(Optional) string with names of extra classes"
    }

    All of the keys of the dict can be passed directly as named parameters of the tag.

    **Tag name**::
        dsfr_select
    **Usage**::
        {% dsfr_select data_dict %}
    """

    allowed_keys = [
        "id",
        "label",
        "onchange",
        "selected",
        "default",
        "options",
        "extra_classes",
    ]
    tag_data = parse_tag_args(args, kwargs, allowed_keys)

    if "id" not in tag_data:
        tag_data["id"] = generate_random_id("select")

    return {"self": tag_data}


@register.inclusion_tag("dsfr/sidemenu.html", takes_context=True)
def dsfr_sidemenu(context: Context, *args, **kwargs) -> dict:
    """
    Returns a side menu item. Takes a dict as parameter, with the following structure:

    data_dict = {
        "title": "The title of the main menu",
        "items": "a list of similarly structured dictionaries (see below)",
        "extra_classes": "(Optional) string with names of extra classes",
    }

    Item-level-dictionaries items can have either links or a sub-level menu list, and
    it can accept three levels of nested menu entries.

    item_dict = {
        "label": "The label of the menu item",
        "items": "(EITHER) a list of similarly structured dictionaries (see below)",
        "link": "(OR) the link (fragment) of the menu item",
    }

    All of the keys of the dict can be passed directly as named parameters of the tag.

    **Tag name**::
        dsfr_sidemenu
    **Usage**::
        {% dsfr_sidemenu data_dict %}
    """

    allowed_keys = ["label", "items", "extra_classes"]
    tag_data = parse_tag_args(args, kwargs, allowed_keys)

    active_path = context["request"].path
    tag_data["items"], _ = find_active_menu_items(tag_data["items"], active_path)

    return {"self": tag_data}


@register.inclusion_tag("dsfr/skiplinks.html", takes_context=True)
def dsfr_skiplinks(context: Context, items: list) -> dict:
    """
    Returns a skiplinks item. Takes a list as parameter, with the following structure:

    items = [{ "link": "item1", "label": "First item title"}, {...}]

    If the list is not passed as a parameter, it extracts it from context.

    **Tag name**::
        dsfr_skiplinks
    **Usage**::
        {% dsfr_skiplinks items %}
    """
    if not items:
        if "skiplinks" in context:
            items = context["skiplinks"]
        else:
            items = {}
    return {"self": {"items": items}}


@register.inclusion_tag("dsfr/summary.html")
def dsfr_summary(items: list) -> dict:
    """
    Returns a summary item. Takes a list as parameter, with the following structure:

    items = [{ "link": "item1", "label": "First item title"}, {...}]

    **Tag name**::
        dsfr_summary
    **Usage**::
        {% dsfr_summary items %}
    """
    return {"self": {"items": items}}


@register.inclusion_tag("dsfr/table.html")
def dsfr_table(*args, **kwargs) -> dict:
    """
    Returns a table item. Takes a dict as parameter, with the following structure:

    data_dict = {
        "caption": "The title of the table",
        "content": list of rows, each row being a list of cells itself,
        "extra_classes": (Optional) string with names of extra classes,
        "header": (Optional) list of cells for the table header
    }

    All of the keys of the dict can be passed directly as named parameters of the tag.

    **Tag name**::
        dsfr_table
    **Usage**::
        {% dsfr_table data_dict %}
    """
    allowed_keys = [
        "caption",
        "content",
        "header",
        "extra_classes",
    ]
    tag_data = parse_tag_args(args, kwargs, allowed_keys)

    return {"self": tag_data}


@register.inclusion_tag("dsfr/tag.html")
def dsfr_tag(*args, **kwargs) -> dict:
    """
    Returns a tag item. Takes a dict as parameter, with the following structure:

    data_dict = {
        "label": "Label of the tag",
        "link": "(Optional) link of the tag",
        "onclick": "(Optional) action that happens when the tag is clicked on",
        "extra_classes: (Optional) string with names of extra classes"
    }

    Relevant extra_classes:
    - fr-tag--sm: for a small tag
    - icon classes: an icon for the tag, along with a positional class (eg, fr-fi-arrow-right-line fr-tag--icon-left)

    All of the keys of the dict can be passed directly as named parameters of the tag.

    **Tag name**::
        dsfr_highlight
    **Usage**::
        {% dsfr_highlight data_dict %}
    """

    allowed_keys = ["label", "link", "onclick", "extra_classes"]
    tag_data = parse_tag_args(args, kwargs, allowed_keys)

    return {"self": tag_data}


@register.inclusion_tag("dsfr/tile.html")
def dsfr_tile(*args, **kwargs) -> dict:
    """
    Returns a tile item. Takes a dict as parameter, with the following structure:

    data_dict = {
        "title": "Title of the tile item",
        "url": "URL of the link of the tile item",
        "image_path": "path of the tile image",
        "extra_classes: (Optional) string with names of extra classes"
    }

    All of the keys of the dict can be passed directly as named parameters of the tag.

    **Tag name**::
        dsfr_tile
    **Usage**::
        {% dsfr_tile data_dict %}
    """
    allowed_keys = [
        "title",
        "url",
        "image_path",
        "extra_classes",
    ]
    tag_data = parse_tag_args(args, kwargs, allowed_keys)

    return {"self": tag_data}


# Other tags and helpers


@register.simple_tag(takes_context=True)
def url_remplace_params(context: Context, **kwargs):
    """
    Allows to make a link that adds or updates a GET parameter while
    keeping the existing ones.
    Useful for combining filters and pagination.

    **Example use**:
    <a href="?{% url_remplace_params page=page_obj.next_page_number %}">Next</a>
    """
    query = context["request"].GET.copy()

    for k in kwargs:
        query[k] = kwargs[k]

    return query.urlencode()


@register.filter
def concatenate(value, arg):
    """Concatenate value and arg"""
    return f"{value}{arg}"


@register.filter
def hyphenate(value, arg):
    """Concatenate value and arg with hyphens as separator, if neither is empty"""
    return "-".join(filter(None, [str(value), str(arg)]))
