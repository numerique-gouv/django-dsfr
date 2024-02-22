from textwrap import dedent

import markdown
from markdown.extensions.codehilite import CodeHiliteExtension
import os

from django.contrib import messages
from django.core.paginator import Paginator
from django.shortcuts import render
from django.urls import reverse
from django.views.decorators.http import require_safe

from dsfr.utils import generate_summary_items

from example_app.forms import ColorForm, ExampleForm

from example_app.dsfr_components import (
    ALL_IMPLEMENTED_COMPONENTS,
    IMPLEMENTED_COMPONENTS,
    EXTRA_COMPONENTS,
    NOT_YET_IMPLEMENTED_COMPONENTS,
)

# Used by the module = getattr(globals()["dsfr_tags"], f"dsfr_{tag_name}") line
from dsfr.templatetags import dsfr_tags  # noqa

# /!\ In order to test formset
from django.views.generic import CreateView
from django.http import HttpResponse
from example_app.forms import AuthorCreateForm, BookCreateFormSet, BookCreateFormHelper
from example_app.models import Author
from example_app.utils import format_markdown_from_file


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

    return {
        "title": page_title,
        "breadcrumb_data": breadcrumb_data,
        "skiplinks": skiplinks,
    }


@require_safe
def index(request):
    payload = init_payload("Accueil")

    payload["summary_data"] = generate_summary_items(
        [
            "Installation",
            "Utilisation",
            "Développement",
            "Notes",
        ]
    )

    return render(request, "example_app/index.html", payload)


@require_safe
def tags_index(request):
    payload = init_payload("Composants")
    payload["documentation"] = format_markdown_from_file("doc/components.md")
    payload["implemented_tags"] = dict(
        sorted(IMPLEMENTED_COMPONENTS.items(), key=lambda k: k[1]["title"])
    )
    payload["extra_tags"] = dict(
        sorted(EXTRA_COMPONENTS.items(), key=lambda k: k[1]["title"])
    )
    payload["not_yet"] = dict(
        sorted(NOT_YET_IMPLEMENTED_COMPONENTS.items(), key=lambda k: k[1]["title"])
    )
    return render(request, "example_app/tags_index.html", payload)


@require_safe
def page_tag(request, tag_name):
    if tag_name in ALL_IMPLEMENTED_COMPONENTS:
        current_tag = ALL_IMPLEMENTED_COMPONENTS[tag_name]
        payload = init_payload(
            current_tag["title"],
            links=[{"url": reverse("tags_index"), "title": "Composants"}],
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

        if "sample_data" in current_tag:
            payload["sample_data"] = current_tag["sample_data"]

        if "doc_url" in current_tag:
            payload["doc_url"] = current_tag["doc_url"]

        sidemenu_items = []
        for key in ALL_IMPLEMENTED_COMPONENTS.keys():
            sidemenu_items.append(
                {"label": key, "link": reverse("page_tag", kwargs={"tag_name": key})}
            )

        payload["side_menu"] = {"title": "Composants", "items": sidemenu_items}
        return render(request, "example_app/page_tag.html", payload)
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
    template_name = "example_app/example_form.html"
    # /!\ Your template needs to extends form_base.html. If you use formset,
    # your template needs to include another template which extends formset_base.html

    def get(self, request, *args, **kwargs):
        instance = None  # noqa: F841
        try:
            if self.object:
                instance = self.object  # noqa: F841
        except Exception:
            self.object = None

        form_class = self.get_form_class()
        form = self.get_form(form_class)
        self.formset = self.get_formset(request)
        formset = self.formset
        book_formhelper = BookCreateFormHelper()  # noqa: F841

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

    def form_valid(self, form, formset):
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

    def form_invalid(self, form, formset):
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
    payload["documentation"] = format_markdown_from_file("CONTRIBUTING.md")

    return render(request, "example_app/doc_markdown.html", payload)


@require_safe
def doc_install(request):
    payload = init_payload("Installation")
    payload["documentation"] = format_markdown_from_file("INSTALL.md")

    return render(request, "example_app/doc_markdown.html", payload)


@require_safe
def doc_form(request):
    payload = init_payload("Formulaires – Documentation")
    payload["documentation"] = format_markdown_from_file("doc/forms.md")

    return render(request, "example_app/doc_markdown.html", payload)


@require_safe
def resource_icons(request):
    payload = init_payload("Icônes")

    icons_root = "dsfr/static/dsfr/dist/icons/"
    icons_folders = os.listdir(icons_root)
    icons_folders.sort()
    all_icons = {}
    for folder in icons_folders:
        files = os.listdir(os.path.join(icons_root, folder))
        files_without_extensions = [f.split(".")[0] for f in files]
        files_without_extensions.sort()
        all_icons[folder] = files_without_extensions

    payload["icons"] = all_icons

    return render(request, "example_app/page_icons.html", payload)


@require_safe
def resource_pictograms(request):
    payload = init_payload("Pictogrammes")

    picto_root = "dsfr/static/dsfr/dist/artwork/pictograms/"
    picto_folders = os.listdir(picto_root)
    picto_folders.sort()
    all_pictos = {}
    for folder in picto_folders:
        files = os.listdir(os.path.join(picto_root, folder))
        files.sort()
        all_pictos[folder] = files

    payload["pictograms"] = all_pictos

    return render(request, "example_app/page_pictograms.html", payload)


@require_safe
def resource_colors(request):
    payload = init_payload("Couleurs")

    form = ColorForm()

    payload["form"] = form
    payload["components_data"] = IMPLEMENTED_TAGS

    return render(request, "example_app/page_colors.html", payload)


@require_safe
def search(request):
    payload = init_payload("Recherche")

    return render(request, "example_app/search.html", payload)
