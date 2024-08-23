from django.conf import settings
from django.test import TestCase, Client
from django.urls import reverse
from django.utils import translation


class DsfrViewTestCase(TestCase):

    def setUp(self) -> None:
        self.client = Client()

    def tearDown(self):
        translation.activate(settings.LANGUAGE_CODE)

    def test_page_is_rendered_in_french_by_default(self) -> None:
        # Checking for strings from both the view and a template
        response = self.client.get(reverse("index"))
        self.assertInHTML(
            "<title>Accueil</title>",
            response.content.decode(),
        )
        self.assertInHTML(
            """<h1 id="fr-theme-modal-title" class="fr-modal__title">Paramètres d’affichage</h1>""",
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
            """<h1 id="fr-theme-modal-title" class="fr-modal__title">Display settings</h1>""",
            response.content.decode(),
        )
