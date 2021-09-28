from django.urls import include, path

urlpatterns = [
    # The "django-dsfr/" prefix is here because this site is deployed as doc on
    # https://entrepreneur-interet-general.github.io/django-dsfr/
    path("django-dsfr/", include("example_app.urls")),
]
