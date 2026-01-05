from itertools import islice
from textwrap import dedent

import markdown
from markdown.extensions.codehilite import CodeHiliteExtension

import os

from django.contrib import messages
from django.core.paginator import Paginator
from django.shortcuts import render
from django.urls import reverse
from django.utils.text import slugify
from django.utils.translation import gettext_lazy as _
from django.views.decorators.http import require_safe

from dsfr.utils import dsfr_version, generate_summary_items

from example_app.forms import AccentColorForm, ExampleForm, FullColorForm

from example_app.dsfr_components import (
    ALL_IMPLEMENTED_COMPONENTS,
    IMPLEMENTED_COMPONENTS,
    EXTRA_COMPONENTS,
    NOT_YET_IMPLEMENTED_COMPONENTS,
    WONT_BE_IMPLEMENTED,
)

# Used by the module = getattr(globals()["dsfr_tags"], f"dsfr_{tag_name}") line
from dsfr.templatetags import dsfr_tags  # noqa

# /!\ In order to test formset
from django.views.generic import CreateView
from django.http import HttpResponse
from example_app.forms import AuthorCreateForm, BookCreateFormSet, BookCreateFormHelper
from example_app.models import Author
from example_app.utils import format_markdown_from_file


def chunks(data, SIZE=10000):
    it = iter(data)
    for _i in range(0, len(data), SIZE):
        yield {k: data[k] for k in islice(it, SIZE)}


def init_payload(page_title: str, links: list = []):
    # Returns the common payload passed to most pages:
    # title: the page title
    # breadcrumb_data: a dictionary used by the page's breadcrumb
    # skiplinks: a list used by the page's skiplinks item

    breadcrumb_data = {
        "current": page_title,
        "links": links,
        "root_dir": "/django-dsfr",
    }

    skiplinks = [
        {"link": "#content", "label": "Contenu"},
        {"link": "#fr-navigation", "label": "Menu"},
    ]

    implemented_component_tags_unsorted = ALL_IMPLEMENTED_COMPONENTS
    implemented_component_tags = dict(
        sorted(
            implemented_component_tags_unsorted.items(), key=lambda k: k[1]["title"]
        )[:31]
        + [
            (
                "see_all",
                {
                    "title": "Voir tous les composants",
                    "url": "/django-dsfr/components/",
                },
            )
        ]
    )

    mega_menu_categories = chunks(implemented_component_tags, 8)

    return {
        "title": page_title,
        "mega_menu_categories": mega_menu_categories,
        "breadcrumb_data": breadcrumb_data,
        "skiplinks": skiplinks,
    }


@require_safe
def index(request):
    payload = init_payload(_("Home page"))  # type: ignore

    payload["summary_data"] = generate_summary_items(
        [
            "Installation",
            "Utilisation",
            "Développement",
            "Notes",
        ]
    )
    payload["dsfr_version"] = dsfr_version()

    return render(request, "example_app/index.html", payload)


@require_safe
def components_index(request):
    payload = init_payload("Composants")
    md = format_markdown_from_file("doc/components.md")
    payload["documentation"] = md["text"]
    payload["implemented_components"] = dict(
        sorted(IMPLEMENTED_COMPONENTS.items(), key=lambda k: k[1]["title"])
    )
    payload["extra_components"] = dict(
        sorted(EXTRA_COMPONENTS.items(), key=lambda k: k[1]["title"])
    )
    not_yet = dict(
        sorted(NOT_YET_IMPLEMENTED_COMPONENTS.items(), key=lambda k: k[1]["title"])
    )
    wont_be = dict(sorted(WONT_BE_IMPLEMENTED.items(), key=lambda k: k[1]["title"]))

    md = markdown.Markdown(
        extensions=[
            "markdown.extensions.fenced_code",
            CodeHiliteExtension(css_class="dsfr-code"),
        ],
    )

    for k, v in not_yet.items():
        if "note" in not_yet[k]:
            not_yet[k]["note"] = (
                md.convert(v["note"]).replace("<p>", "").replace("</p>", "")
            )
    payload["not_yet"] = not_yet

    for k, v in wont_be.items():
        wont_be[k]["reason"] = (
            md.convert(v["reason"]).replace("<p>", "").replace("</p>", "")
        )
    payload["wont_be"] = wont_be
    return render(request, "example_app/components_index.html", payload)


@require_safe
def page_component(request, tag_name):  # NOSONAR
    sidemenu_implemented_items = []
    for key, value in ALL_IMPLEMENTED_COMPONENTS.items():
        sidemenu_implemented_items.append(
            {
                "label": f"{value['title']} ({key})",
                "link": reverse("page_component", kwargs={"tag_name": key}),
            }
        )

    sidemenu_implemented = {
        "label": "Composants implémentés",
        "items": sidemenu_implemented_items,
    }

    if "/components/" in request.path:
        sidemenu_implemented["is_active"] = True

    side_menu = {
        "items": [
            {"label": "Documentation", "link": reverse("components_index")},
            sidemenu_implemented,
            {
                "label": "Composants non implémentés",
                "link": reverse("components_index")
                + "#tabpanel-notyetimplemented-panel",
            },
        ]
    }

    payload_links = [{"url": reverse("components_index"), "title": "Composants"}]

    # First three ifs are components with a dedicated markdown doc.
    if tag_name == "footer":
        payload = init_payload(
            page_title="Pied de page",
            links=payload_links,
        )
        md = format_markdown_from_file("doc/footer.md")
        payload["documentation"] = md["text"]
        payload["side_menu"] = side_menu
        return render(request, "example_app/doc_markdown_with_sidebar.html", payload)
    elif tag_name == "header":
        payload = init_payload(
            page_title="En-tête",
            links=payload_links,
        )

        md = format_markdown_from_file("doc/header.md")
        payload["documentation"] = md["text"]
        payload["side_menu"] = side_menu
        return render(request, "example_app/doc_markdown_with_sidebar.html", payload)

    elif tag_name == "follow":
        payload = init_payload(
            page_title="Lettre d’information et Réseaux Sociaux",
            links=payload_links,
        )
        md = format_markdown_from_file("doc/follow.md")
        payload["documentation"] = md["text"]
        payload["side_menu"] = side_menu
        return render(request, "example_app/doc_markdown_with_sidebar.html", payload)
    elif tag_name in ALL_IMPLEMENTED_COMPONENTS:
        current_tag = ALL_IMPLEMENTED_COMPONENTS[tag_name]
        payload = init_payload(
            current_tag["title"],
            links=payload_links,
        )
        payload["tag_name"] = tag_name

        # Tag-specific context
        if tag_name == "pagination":
            sample_content = list(range(0, 100))
            paginator = Paginator(sample_content, 10)
            payload["page_obj"] = paginator.get_page(4)
        elif tag_name == "django_messages":
            messages.info(request, "Ceci est une information")
            messages.success(request, "Ceci est un succès")
            messages.warning(request, "Ceci est un avertissement")
            messages.error(request, "Ceci est une erreur")

        module = getattr(globals()["dsfr_tags"], f"dsfr_{tag_name}")
        payload["tag_comment"] = markdown.markdown(
            dedent(module.__doc__),
            extensions=[
                "markdown.extensions.tables",
                "md_in_html",
                "markdown.extensions.fenced_code",
                CodeHiliteExtension(css_class="dsfr-code"),
            ],
        )

        keys = ["sample_data", "doc_url", "example_url", "storybook_url"]
        for k in keys:
            if k in current_tag:
                payload[k] = current_tag[k]

        payload["side_menu"] = side_menu
        return render(request, "example_app/page_component.html", payload)
    else:
        payload = init_payload("Non implémenté")
        payload["not_yet"] = {
            "text": "Le contenu recherché n’est pas encore implémenté",
            "title": "Non implémenté",
        }
        return render(request, "example_app/not_yet.html", payload)


def page_form(request):
    if request.method == "POST":
        # create a form instance and populate it with data from the request:
        form = ExampleForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            # return HttpResponseRedirect("/thanks/")
            pass

    # if a GET (or any other method) we'll create a blank form
    else:
        form = ExampleForm()

    payload = init_payload(
        "Formulaire basique",
        links=[{"url": reverse("doc_form"), "title": "Formulaires"}],
    )
    payload["form"] = form

    return render(request, "example_app/page_form.html", payload)


# /!\ Example view for form and formset
class AuthorCreateView(CreateView):
    model = Author
    form_class = AuthorCreateForm
    formset = None
    template_name = "example_app/page_formset_main_form.html"
    # /!\ Your template needs to extends form_base.html. If you use formset,
    # your template needs to include another template which extends formset_base.html

    def get(self, request, *args, **kwargs):
        instance = None  # noqa: F841 NOSONAR
        try:
            if self.object:
                instance = self.object  # noqa: F841
        except Exception:
            self.object = None

        form_class = self.get_form_class()
        form = self.get_form(form_class)
        self.formset = self.get_formset(request)
        formset = self.formset
        book_formhelper = BookCreateFormHelper()  # noqa: F841 NOSONAR

        return self.render_to_response(
            self.get_context_data(form=form, formset=formset)
        )

    def get_formset(self, request, instance=None):
        if request.POST and instance:
            self.formset = BookCreateFormSet(
                request.POST,
                request.FILES,
                instance=instance,
            )
        else:
            self.formset = BookCreateFormSet()
        return self.formset

    def get_context_data(self, **kwargs):
        context = super(AuthorCreateView, self).get_context_data(**kwargs)

        payload = init_payload(
            "Formulaire avec formset",
            links=[{"url": reverse("doc_form"), "title": "Formulaires"}],
        )

        for key, value in payload.items():
            context[key] = value

        book_formhelper = BookCreateFormHelper()

        instance = None
        try:
            if self.object:
                instance = self.object
        except Exception:
            self.object = None

        # /!\ Pass your form, formset and helper to the context
        if self.request.POST:
            context["form"] = self.form_class(self.request.POST)
            context["formset"] = BookCreateFormSet(
                self.request.POST, self.request.FILES, instance=instance
            )
            context["book_formhelper"] = book_formhelper
        else:
            context["form"] = self.form_class()
            self.formset = self.get_formset(self.request)
            context["formset"] = self.formset
            context["book_formhelper"] = book_formhelper

        context["object_name"] = "book"

        # /!\ Don't forget your dsfr button
        context["btn_submit"] = {
            "label": "Soumettre",
            "onclick": "",
            "type": "submit",
        }
        return context

    def post(self, request, *args, **kwargs):
        instance = None
        try:
            if self.object:
                instance = self.object
        except Exception:
            self.object = None

        form_class = self.get_form_class()
        form = self.get_form(form_class)
        formset = BookCreateFormSet(
            self.request.POST, self.request.FILES, instance=instance
        )

        if form.is_valid() and formset.is_valid():
            return self.form_valid(form, formset)
        return self.form_invalid(form, formset)

    def form_valid(self, form, formset):  # type: ignore
        """
        Called if all forms are valid. Creates a Author instance along
        with associated books and then redirects to a success page.
        """

        self.object = form.save()
        formset.instance = (
            self.object
        )  # /!\ Before saving formset, link it to the object created with the main form
        formset.save()

        return HttpResponse(b"Success !")

    def form_invalid(self, form, formset):  # type: ignore
        """
        Called if whether a form is invalid. Re-renders the context
        data with the data-filled forms and errors.
        """
        return self.render_to_response(
            self.get_context_data(form=form, formset=formset)
        )


@require_safe
def doc_contributing(request):
    payload = init_payload("Contribuer à Django-DSFR")
    md = format_markdown_from_file("CONTRIBUTING.md", ignore_first_line=True)
    payload["documentation"] = md["text"]
    payload["summary_data"] = md["summary"]

    return render(request, "example_app/doc_markdown.html", payload)


@require_safe
def doc_install(request):
    payload = init_payload("Installation de Django-DSFR")

    md = format_markdown_from_file("INSTALL.md", ignore_first_line=True)
    payload["documentation"] = md["text"]
    payload["summary_data"] = md["summary"]

    return render(request, "example_app/doc_markdown.html", payload)


@require_safe
def doc_usage(request):
    payload = init_payload("Utiliser Django-DSFR")

    md = format_markdown_from_file("doc/usage.md")
    payload["documentation"] = md["text"]
    payload["summary_data"] = md["summary"]

    return render(request, "example_app/doc_markdown.html", payload)


@require_safe
def doc_form(request):
    payload = init_payload("Formulaires – Documentation")
    md = format_markdown_from_file("doc/forms.md", ignore_first_line=True)
    payload["documentation"] = md["text"]
    # payload["summary_data"] = md["summary"]

    return render(request, "example_app/doc_markdown.html", payload)


@require_safe
def resource_colors(request):
    payload = init_payload("Couleurs")

    accent_color_form = AccentColorForm()
    full_color_form = FullColorForm()

    payload["accent_color_form"] = accent_color_form
    payload["full_color_form"] = full_color_form
    payload["components_data"] = IMPLEMENTED_COMPONENTS

    return render(request, "example_app/page_colors.html", payload)


@require_safe
def resource_icons(request):
    payload = init_payload("Icônes")

    icons_root = "dsfr/static/dsfr/dist/icons/"
    icons_folders = os.listdir(icons_root)
    icons_folders.sort()
    all_icons = {}
    summary = []
    for folder in icons_folders:
        files = os.listdir(os.path.join(icons_root, folder))
        files_without_extensions = [f.split(".")[0].replace("fr--", "") for f in files]
        files_without_extensions.sort()
        all_icons[folder] = files_without_extensions
        summary.append({"link": f"#{slugify(folder)}", "label": folder.capitalize()})

    payload["icons"] = all_icons
    payload["summary"] = summary

    return render(request, "example_app/page_icons.html", payload)


@require_safe
def resource_pictograms(request):
    payload = init_payload("Pictogrammes")

    picto_root = "dsfr/static/dsfr/dist/artwork/pictograms/"
    picto_folders = os.listdir(picto_root)
    picto_folders.sort()
    all_pictos = {}
    summary = []
    for folder in picto_folders:
        files = os.listdir(os.path.join(picto_root, folder))
        files.sort()
        all_pictos[folder] = files
        summary.append({"link": f"#{slugify(folder)}", "label": folder.capitalize()})

    payload["pictograms"] = all_pictos
    payload["summary"] = summary

    return render(request, "example_app/page_pictograms.html", payload)


@require_safe
def resource_templatetags(request):
    payload = init_payload("Balises et filtres personalisés")
    payload["strfmt_example_args"] = [1 + 2, "awesome"]
    payload["strfmt_example_kwargs"] = {
        "add_result": 1 + 2,
        "result_feeling": "awesome",
    }

    return render(request, "example_app/page_templatetags.html", payload)


@require_safe
def resource_markdown(request):
    payload = init_payload("Extension : rendu de Markdown")

    payload.update(
        {
            "samples": {
                "Classe personnalisée": """#### Titre 4 affiché comme titre 6 {: .fr-h6 }""",
                "Lien externe": "Texte contenant [un lien vers un autre site](https://www.systeme-de-design.gouv.fr/)",
                "Mise en exergue": """!! note ""
    Texte de la mise en exergue.
                """,
                "Mise en avant minimale": """!!! note ""
    Texte de la mise en avant.
                """,
                "Mise en avant avec titre": """!!! note "Attention !"
    Texte de la mise en avant.
                """,
                "Mise en avant avec titre et icône": """!!! warning-line "Attention !"
    Texte de la mise en avant.
                """,
                "Citation": """> Texte d’une citation…
qui peut être sur plusieurs lignes.

Jusqu’à la prochaine ligne vide.""",
                "Tableau simple": """
    | Colonne 1          | Colonne 2          |
    |--------------------|--------------------|
    | Ligne 1, colonne 1 | Ligne 1, colonne 2 |
    | Ligne 2, colonne 1 | Ligne 2, colonne 2 |
    """,
            }
        }
    )
    payload.update(
        {
            "samples_summary": [
                {"link": f"#sample-{slugify(sample)}", "label": sample}
                for sample in payload["samples"]
            ]
        }
    )

    return render(request, "example_app/page_markdown.html", payload)


@require_safe
def search(request):
    payload = init_payload("Recherche")

    return render(request, "example_app/search.html", payload)
