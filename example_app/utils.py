import markdown
from markdown.extensions.codehilite import CodeHiliteExtension
from markdown.extensions.toc import TocExtension
from example_app.models import Genre


def populate_genre_choices():
    # ModelMultipleChoiceField won't show individual help_text
    # So instead, we use MultipleChoiceField
    # And instead of a queryset, MultipleChoiceField requires a list of choices
    # We have to format our queryset into a list of choices including help_texts
    # In this example, the help_text for each object is the field object.help_text in database

    genres_list = []

    for genre in Genre.objects.all():
        if not genre.help_text:
            to_add = (
                genre.pk,
                genre.designation,
            )  # If no help_text, a tuple (pk, designation) as in BOOK_FORMAT
        else:
            to_add = (
                genre.pk,
                {"label": genre.designation, "help_text": genre.help_text},
            )  # If help_text, a tuple (pk, {'label':designation, 'help_text':help_text}) as in BOOK_FORMAT
        genres_list.append(to_add)

    return genres_list


def format_markdown_from_file(filename: str, ignore_first_line: bool = False) -> dict:
    with open(filename) as f:
        md = markdown.Markdown(
            extensions=[
                "markdown.extensions.fenced_code",
                TocExtension(toc_depth="2-6"),
                CodeHiliteExtension(css_class="dsfr-code"),
            ],
        )

        if ignore_first_line:
            content = "".join(f.readlines()[1:]).strip()
        else:
            content = f.read()

        text = md.convert(content)

        toc = md.toc_tokens

        summary = md_format_toc(toc)

        return {"text": text, "summary": summary}


def md_format_toc(toc: dict) -> list:
    # Format the generated TOC into a Django-DSFR summary dict
    summary_level = []
    for item in toc:
        if len(item["children"]):
            children = md_format_toc(item["children"])
            summary_level.append(
                {"link": f"#{item['id']}", "label": item["name"], "children": children}
            )
        else:
            summary_level.append({"link": f"#{item['id']}", "label": item["name"]})

    return summary_level
