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


# Lorem ipsum paragraphs
lorem_ipsum = """
<p class="fr-mb-2w">
    Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut
    labore et dolore magna aliqua. At quis risus sed vulputate odio ut enim. At risus viverra
    adipiscing at in tellus integer feugiat. Aliquam purus sit amet luctus venenatis lectus.
    Pellentesque id nibh tortor id aliquet lectus proin. Ultricies leo integer malesuada nunc vel
    risus. Euismod elementum nisi quis eleifend quam adipiscing vitae proin. Iaculis eu non diam
    phasellus vestibulum lorem sed risus ultricies. Quis varius quam quisque id diam. Vehicula
    ipsum a arcu cursus vitae congue mauris rhoncus. Sed id semper risus in hendrerit gravida.
</p>

<p class="fr-mb-2w">
    Suspendisse potenti nullam ac tortor vitae purus faucibus. Condimentum lacinia quis vel eros.
    Pellentesque sit amet porttitor eget dolor. Varius duis at consectetur lorem donec massa sapien
    faucibus. Egestas pretium aenean pharetra magna ac placerat vestibulum lectus. Tristique magna
    sit amet purus gravida. Nec ullamcorper sit amet risus nullam eget felis eget nunc. Aenean vel
    elit scelerisque mauris pellentesque pulvinar. Vitae proin sagittis nisl rhoncus mattis rhoncus
    urna neque viverra. Quam viverra orci sagittis eu volutpat odio. Sapien faucibus et molestie
    ac. Rhoncus aenean vel elit scelerisque mauris pellentesque pulvinar pellentesque. Nunc sed
    velit dignissim sodales ut eu sem integer.
</p>

<p class="fr-mb-2w">
    Diam maecenas ultricies mi eget mauris pharetra et ultrices. Justo nec ultrices dui sapien eget
    mi proin. Viverra mauris in aliquam sem fringilla ut. Pretium lectus quam id leo in vitae
    turpis massa. Ultricies integer quis auctor elit sed vulputate mi sit amet. Non quam lacus
    suspendisse faucibus interdum posuere lorem. Feugiat in fermentum posuere urna nec. Bibendum
    enim facilisis gravida neque. Vitae aliquet nec ullamcorper sit amet risus. Et netus et
    malesuada fames ac turpis. Ut eu sem integer vitae. Aliquam eleifend mi in nulla posuere
    sollicitudin aliquam ultrices sagittis. Eget sit amet tellus cras adipiscing enim. Massa eget
    egestas purus viverra accumsan. Urna neque viverra justo nec. Bibendum est ultricies integer
    quis auctor elit. Sagittis vitae et leo duis ut diam.
</p>

<p class="fr-mb-2w">
    Urna porttitor rhoncus dolor purus. Enim eu turpis egestas pretium. Risus ultricies tristique
    nulla aliquet enim tortor at auctor urna. Etiam non quam lacus suspendisse faucibus interdum
    posuere lorem. Ut enim blandit volutpat maecenas volutpat blandit aliquam etiam. Ac tortor
    vitae purus faucibus ornare suspendisse sed nisi lacus. Accumsan lacus vel facilisis volutpat
    est velit egestas dui. Enim eu turpis egestas pretium aenean pharetra. Arcu cursus vitae congue
    mauris rhoncus. A cras semper auctor neque vitae tempus. Viverra ipsum nunc aliquet bibendum
    enim facilisis gravida neque convallis. Ac tortor dignissim convallis aenean et tortor. Sed id
    semper risus in hendrerit gravida rutrum. Tempus iaculis urna id volutpat lacus laoreet.
</p>

<p class="fr-mb-2w">
    Massa tempor nec feugiat nisl pretium fusce. Urna porttitor rhoncus dolor purus non enim
    praesent. Suspendisse ultrices gravida dictum fusce. Habitant morbi tristique senectus et netus.
    Adipiscing vitae proin sagittis nisl. Bibendum ut tristique et egestas quis. Dictum non
    consectetur a erat nam at lectus. Vulputate dignissim suspendisse in est ante in nibh mauris
    cursus. Faucibus turpis in eu mi bibendum neque egestas congue quisque. Neque laoreet
    suspendisse interdum consectetur libero id faucibus. Gravida rutrum quisque non tellus orci ac
    auctor augue mauris. Turpis nunc eget lorem dolor sed viverra ipsum nunc. Quam viverra orci
    sagittis eu volutpat odio. Id interdum velit laoreet id donec ultrices tincidunt arcu non.
    Viverra nibh cras pulvinar mattis nunc sed. Risus sed vulputate odio ut enim blandit volutpat
    maecenas volutpat. Augue neque gravida in fermentum et sollicitudin ac orci. Commodo odio
    aenean sed adipiscing diam.
</p>
"""
