import unittest
from django.test import Client
from django.urls import reverse

from example_app.dsfr_components import ALL_TAGS


class BasicPagesTest(unittest.TestCase):
    def setUp(self):
        self.client = Client()

    def test_index(self):
        response = self.client.get(reverse("index"))
        self.assertEqual(response.status_code, 200)

    def test_page_search(self):
        response = self.client.get(reverse("page_search"))
        self.assertEqual(response.status_code, 200)


class DocTest(unittest.TestCase):
    def setUp(self):
        self.client = Client()

    def test_doc_contributing(self):
        response = self.client.get(reverse("doc_contributing"))
        self.assertEqual(response.status_code, 200)

    def test_doc_install(self):
        response = self.client.get(reverse("doc_install"))
        self.assertEqual(response.status_code, 200)


class ComponentsTest(unittest.TestCase):

    def setUp(self):
        self.client = Client()

    def test_components_index(self):
        response = self.client.get(reverse("example_app:components_index"))
        self.assertEqual(response.status_code, 200)

    def test_each_component(self):
        for key in ALL_TAGS.keys():
            response = self.client.get(
                reverse("page_component", kwargs={"tag_name": key})
            )
            self.assertEqual(response.status_code, 200)


class FormsTest(unittest.TestCase):
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


class ResourceTest(unittest.TestCase):
    def setUp(self):
        self.client = Client()

    def test_resource_icons(self):
        response = self.client.get(reverse("resource_icons"))
        self.assertEqual(response.status_code, 200)

    def test_resource_pictograms(self):
        response = self.client.get(reverse("resource_pictograms"))
        self.assertEqual(response.status_code, 200)
