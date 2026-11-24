from django.test import SimpleTestCase
from dsfr.utils import generate_random_id, generate_summary_items, parse_tag_args


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


class TestParseTagArgs(SimpleTestCase):
    def test_parse_tag_args_with_args_only(self):
        self.assertEqual(
            parse_tag_args([{"coucou": "youpi"}], {}, ["coucou"]), {"coucou": "youpi"}
        )

    def test_parse_tag_args_with_kwargs_only(self):
        self.assertEqual(
            parse_tag_args(None, {"coucou": "youpi"}, ["coucou"]), {"coucou": "youpi"}
        )

    def test_parse_tag_args_with_data_attributes(self):
        self.assertEqual(
            parse_tag_args(
                [{}],
                {"data_test": "value", "data_another": "thing"},
                [],
            ),
            {"data_attributes": {"test": "value", "another": "thing"}},
        )

    def test_parse_tag_args_with_allowed_and_data_attributes(self):
        self.assertEqual(
            parse_tag_args(
                [{"foo": "bar"}],
                {"coucou": "yes", "data_role": "admin"},
                ["coucou", "foo"],
            ),
            {"foo": "bar", "coucou": "yes", "data_attributes": {"role": "admin"}},
        )

    def test_parse_tag_args_with_disallowed_keys(self):
        # "not_allowed" should be ignored completely
        self.assertEqual(
            parse_tag_args(None, {"not_allowed": "oops"}, ["coucou"]),
            {},
        )

    def test_parse_tag_args_with_empty_inputs(self):
        self.assertEqual(
            parse_tag_args(None, {}, []),
            {},
        )
