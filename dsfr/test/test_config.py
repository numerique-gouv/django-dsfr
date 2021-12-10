from django.test import TestCase, Client, override_settings
from django.urls import reverse
from dsfr.models import DsfrConfig


class DsfrConfigTestCase(TestCase):
    def setUp(self) -> None:
        DsfrConfig.objects.create()

    def test_config_is_created(self) -> None:
        test_item = DsfrConfig.objects.first()
        self.assertEqual(test_item.site_title, "Titre du site")


class ContextProcessorTestCase(TestCase):
    def setUp(self) -> None:
        self.client = Client()

    def test_config_is_none_if_not_created_yet(self) -> None:
        response = self.client.get(reverse("index"))
        self.assertEqual(response.context["SITE_CONFIG"], None)

    def test_config_is_available_to_templates(self) -> None:
        DsfrConfig.objects.create()
        response = self.client.get(reverse("index"))
        self.assertEqual(response.context["SITE_CONFIG"].site_title, "Titre du site")
