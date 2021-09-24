from django.core.paginator import Page
from django.utils.text import slugify
import random
import string


def list_pages(page_obj: Page) -> Page:
    """
    Gets a paginator page item and returns it with a list of pages to display like:
    [1, 2, "…", 17, 18, 19, "…" 41, 42]

    Currently not in use, simpler pages lists are implemented.
    """
    last_page_number = page_obj.paginator.num_pages
    pages_list = [1, 2]
    if page_obj.number > 1:
        pages_list.append(page_obj.number - 1)
    pages_list.append(page_obj.number)
    if page_obj.number < last_page_number:
        pages_list.append(page_obj.number + 1)
    pages_list.append(last_page_number - 1)
    pages_list.append(last_page_number)

    # Keep only one of each
    unique_pages_items = list(set(pages_list))

    list_with_separators = [unique_pages_items[0]]

    for i in range(1, len(unique_pages_items)):
        difference = unique_pages_items[i] - unique_pages_items[i - 1]
        # If "…" would replace only one value, show it instead
        if difference == 2:
            list_with_separators.append(unique_pages_items[i - 1] + 1)
        elif difference > 1:
            list_with_separators.append("…")
        list_with_separators.append(unique_pages_items[i])

    page_obj.pages_list = list_with_separators
    return page_obj


def parse_tag_args(args, kwargs, allowed_keys: list) -> dict:
    """
    Allows to use a tag with either all the arguments in a dict or by declaring them separately
    """
    if args:
        tag_data = args[0]
    else:
        tag_data = {}

    for k in kwargs:
        if k in allowed_keys:
            tag_data[k] = kwargs[k]

    return tag_data


def find_active_menu_items(menu: list, active_path: str) -> list:
    """
    Utility function for the dsfr_sidemenu tag: recusively locates the current
    active page and its parent menus and sets them to active
    """
    for key, item in enumerate(menu):  # Level 1 items
        if "items" in item:
            item["items"], set_active = find_active_menu_items(
                item["items"], active_path
            )
            if set_active:
                menu[key]["is_active"] = True
        else:
            if item["link"] == active_path:
                menu[key]["is_active"] = True
                set_active = True
            else:
                menu[key]["is_active"] = False
                set_active = False
    return menu, set_active


def generate_random_id(start: str = ""):
    """
    Generates a random alphabetic id.
    """
    result = "".join(random.SystemRandom().choices(string.ascii_lowercase, k=16))
    if start:
        result = "-".join([start, result])
    return result


def generate_summary_items(sections_names: list) -> list:
    """
    Takes a list of section names and returns them as a list of links
    that can be used with dsfr_summary or dsfr_menu tags.
    """
    items = []
    for section_name in sections_names:
        items.append(
            {
                "label": section_name,
                "link": f"#{slugify(section_name)}",
            }
        )

    return items
