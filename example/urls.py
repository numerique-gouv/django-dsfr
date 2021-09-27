from django.urls import include, path

urlpatterns = [
    path("django-dsfr/", include("example_app.urls")),
]
