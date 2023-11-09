import markdown
from markdown.extensions.codehilite import CodeHiliteExtension
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


def format_markdown_from_file(filename: str) -> str:
    with open(filename) as f:
        content = f.read()
        return markdown.markdown(
            content,
            extensions=[
                "markdown.extensions.fenced_code",
                CodeHiliteExtension(css_class="dsfr-code"),
            ],
        )
