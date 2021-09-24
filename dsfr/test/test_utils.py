from django.test import SimpleTestCase
from dsfr.utils import generate_random_id, generate_summary_items


class GenerateRandomIdTestCase(SimpleTestCase):
    def test_generate_basic_id(self):
        test_id = generate_random_id()
        self.assertEqual(len(test_id), 16)

    def test_generate_id_with_prefix(self):
        test_id = generate_random_id("test")
        self.assertEqual(test_id[:5], "test-")
        self.assertEqual(len(test_id), 21)

    def test_generate_id_with_empty_prefix(self):
        test_id = generate_random_id("")
        self.assertEqual(len(test_id), 16)


class GenerateSummaryItemsTestCase(SimpleTestCase):
    def test_generate_summary_items(self):
        test_data = ["Premier élément", "Second élément", "Dernier"]
        test_summary = generate_summary_items(test_data)
        self.assertEqual(
            test_summary,
            [
                {"label": "Premier élément", "link": "#premier-element"},
                {"label": "Second élément", "link": "#second-element"},
                {"label": "Dernier", "link": "#dernier"},
            ],
        )
