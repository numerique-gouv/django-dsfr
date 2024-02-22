from django_distill import distill_path

from example_app.views import (
    index,
    resource_colors,
    resource_icons,
    resource_pictograms,
    tags_index,
    page_form,
    page_tag,
    AuthorCreateView,
    doc_contributing,
    doc_install,
    doc_form,
    search,
)
from example_app.dsfr_components import ALL_TAGS


def get_all_tags():
    for key in ALL_TAGS:
        yield ({"tag_name": key})


urlpatterns = [
    distill_path("", index, name="index", distill_file="django-dsfr/index.html"),
    distill_path(
        "doc-contributing",
        doc_contributing,
        name="doc_contributing",
        distill_file="django-dsfr/doc-contributing/index.html",
    ),
    distill_path(
        "doc-install",
        doc_install,
        name="doc_install",
        distill_file="django-dsfr/doc-install/index.html",
    ),
    distill_path(
        "tags/",
        tags_index,
        name="tags_index",
        distill_file="django-dsfr/tags/index.html",
    ),
    distill_path(
        "tags/<slug:tag_name>/",
        page_tag,
        name="page_tag",
        distill_func=get_all_tags,
    ),
    distill_path(
        "form/",
        doc_form,
        name="doc_form",
        distill_file="django-dsfr/form/index.html",
    ),
    distill_path(
        "form/example/",
        page_form,
        name="page_form",
        distill_file="django-dsfr/form/example/index.html",
    ),
    distill_path(
        "form/example-formset/",
        AuthorCreateView.as_view(),
        name="form_formset",
        distill_file="django-dsfr/form/example-formset/index.html",
    ),
    distill_path(
        "resources/colors",
        resource_colors,
        name="resource_colors",
        distill_file="django-dsfr/resources/colors/index.html",
    ),
    distill_path(
        "resources/icons",
        resource_icons,
        name="resource_icons",
        distill_file="django-dsfr/resources/icons/index.html",
    ),
    distill_path(
        "resources/pictograms",
        resource_pictograms,
        name="resource_pictograms",
        distill_file="django-dsfr/resources/pictograms/index.html",
    ),
    distill_path(
        "search/",
        search,
        name="page_search",
        distill_file="django-dsfr/search/index.html",
    ),
]
