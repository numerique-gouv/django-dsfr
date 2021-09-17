from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<slug:tag_name>/", views.page_tag, name="page_tag"),
    path("tests", views.page_tests, name="page_tests"),
]
