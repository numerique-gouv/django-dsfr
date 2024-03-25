from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import include, path
from django.views.generic import RedirectView

urlpatterns = [
    # The "django-dsfr/" prefix is here because this site is deployed as doc on
    # https://numerique-gouv.github.io/django-dsfr/
    path("admin/", admin.site.urls),
    path("django-dsfr/", include("example_app.urls")),
    path("", RedirectView.as_view(pattern_name="index", permanent=False)),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
