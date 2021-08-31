from django.urls import include, path

urlpatterns = [
    path("", include("example_app.urls")),
]
