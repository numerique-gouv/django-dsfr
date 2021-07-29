from django.core.paginator import Page


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
