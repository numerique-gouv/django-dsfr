from django.conf import settings
from django.test import Client, TestCase
from django.urls import reverse
from django.utils import translation

from example_app.dsfr_components import ALL_TAGS


class BasicPagesTest(TestCase):
    def setUp(self) -> None:
        self.client = Client()

    def tearDown(self) -> None:
        translation.activate(settings.LANGUAGE_CODE)

    def test_index(self):
        response = self.client.get(reverse("index"))
        self.assertEqual(response.status_code, 200)

    def test_page_search(self):
        response = self.client.get(reverse("page_search"))
        self.assertEqual(response.status_code, 200)

    def test_page_is_rendered_in_french_by_default(self) -> None:
        # Checking for strings from both the view and a template
        response = self.client.get(reverse("index"))
        self.assertInHTML(
            "<title>Accueil</title>",
            response.content.decode(),
        )
        self.assertInHTML(
            """<h2 id="fr-theme-modal-title" class="fr-modal__title">Paramètres d’affichage</h2>""",
            response.content.decode(),
        )

    def test_page_can_be_rendered_in_english(self) -> None:
        # Checking for strings from both the view and a template
        self.client.cookies.load({settings.LANGUAGE_COOKIE_NAME: "en"})
        response = self.client.get(reverse("index"))
        self.assertInHTML(
            "<title>Home page</title>",
            response.content.decode(),
        )
        self.assertInHTML(
            """<h2 id="fr-theme-modal-title" class="fr-modal__title">Display settings</h2>""",
            response.content.decode(),
        )


class DocTest(TestCase):
    def setUp(self):
        self.client = Client()

    def test_doc_contributing(self):
        response = self.client.get(reverse("doc_contributing"))
        self.assertEqual(response.status_code, 200)

    def test_doc_install(self):
        response = self.client.get(reverse("doc_install"))
        self.assertEqual(response.status_code, 200)


class ComponentsTest(TestCase):
    def setUp(self):
        self.client = Client()

    def test_components_index(self):
        response = self.client.get(reverse("components_index"))
        self.assertEqual(response.status_code, 200)

    def test_each_component(self):
        for key in ALL_TAGS.keys():
            response = self.client.get(
                reverse("page_component", kwargs={"tag_name": key})
            )
            self.assertEqual(response.status_code, 200)


class FormsTest(TestCase):
    def setUp(self):
        self.client = Client()

    def test_doc_form(self):
        response = self.client.get(reverse("doc_form"))
        self.assertEqual(response.status_code, 200)

    def test_page_form(self):
        response = self.client.get(reverse("page_form"))
        self.assertEqual(response.status_code, 200)

    def test_form_formset(self):
        response = self.client.get(reverse("form_formset"))
        self.assertEqual(response.status_code, 200)


class ResourceTest(TestCase):
    def setUp(self):
        self.client = Client()

    def test_resource_icons(self):
        response = self.client.get(reverse("resource_icons"))
        self.assertEqual(response.status_code, 200)

    def test_resource_pictograms(self):
        response = self.client.get(reverse("resource_pictograms"))
        self.assertEqual(response.status_code, 200)
