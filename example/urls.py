from django.urls import include, path
from django.views.generic import RedirectView

urlpatterns = [
    # The "django-dsfr/" prefix is here because this site is deployed as doc on
    # https://entrepreneur-interet-general.github.io/django-dsfr/
    path("django-dsfr/", include("example_app.urls")),
    path("", RedirectView.as_view(pattern_name="index", permanent=False)),
]
