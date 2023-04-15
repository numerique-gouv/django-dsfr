from django_distill import distill_path

from example_app.views import index, tags_index, page_form, page_tag, AuthorCreateView
from .tag_specifics import ALL_TAGS


def get_all_tags():
    for key in ALL_TAGS:
        yield ({"tag_name": key})


urlpatterns = [
    distill_path("", index, name="index", distill_file="django-dsfr/index.html"),
    distill_path(
        "tags/",
        tags_index,
        name="tags_index",
        distill_file="django-dsfr/tags/index.html",
    ),
    distill_path(
        "form/",
        page_form,
        name="page_form",
        distill_file="django-dsfr/form/index.html",
    ),
    distill_path(
        "tags/<slug:tag_name>/",
        page_tag,
        name="page_tag",
        distill_func=get_all_tags,
    ),
    distill_path(
        "form_formset/",
        AuthorCreateView.as_view(),
        name="form_formset",
        distill_file="django-dsfr/example-form.html",
    ),
]
