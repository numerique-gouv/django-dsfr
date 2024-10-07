from enum import auto
from unittest import skipIf

from django.db.models import IntegerChoices
from django.test import SimpleTestCase
from django.utils.safestring import mark_safe
from django.utils.version import PY311

from dsfr.enums import ExtendedChoices

if PY311:
    from enum import property as enum_property, nonmember
else:
    from types import DynamicClassAttribute as enum_property


class ExtendedChoicesTestCase(SimpleTestCase):
    def test_create_dict_enum(self):
        class TestExtendedChoices(ExtendedChoices, IntegerChoices):
            TEST_1 = {
                "value": auto(),
                "label": "Test 1",
            }
            TEST_2 = {
                "value": auto(),
                "label": "Test 2",
            }

        self.assertEqual(
            {(1, "Test 1"), (2, "Test 2")}, set(TestExtendedChoices.choices)
        )
        self.assertEqual({"Test 1", "Test 2"}, set(TestExtendedChoices.labels))
        self.assertEqual({"TEST_1", "TEST_2"}, set(TestExtendedChoices.names))
        self.assertEqual({1, 2}, set(TestExtendedChoices.values))

    def test_additional_attributes(self):
        class TestExtendedChoices(ExtendedChoices, IntegerChoices):
            TEST_1 = {
                "value": auto(),
                "additionnal_attribute_1": {"lorem": "ipsum 1"},
                "additionnal_attribute_2": mark_safe(
                    "<strong>Item 1</strong>"
                ),  # nosec
            }
            TEST_2 = {
                "value": auto(),
                "additionnal_attribute_1": {"lorem": "ipsum 2"},
                "additionnal_attribute_2": mark_safe(
                    "<strong>Item 2</strong>"
                ),  # nosec
            }

        self.assertEqual(
            {"additionnal_attribute_1", "additionnal_attribute_2"},
            set(TestExtendedChoices.additional_attributes),
        )
        self.assertEqual(
            [{"lorem": "ipsum 1"}, {"lorem": "ipsum 2"}],
            [it.additionnal_attribute_1 for it in TestExtendedChoices],
        )
        self.assertEqual(
            {"<strong>Item 1</strong>", "<strong>Item 2</strong>"},
            {it.additionnal_attribute_2 for it in TestExtendedChoices},
        )

    @skipIf(not PY311, "'enum.nonmember' was added to Python 3.11")
    def test_nonmember_attributes(self):
        class TestExtendedChoices(ExtendedChoices, IntegerChoices):
            TEST_1 = {"value": auto()}
            TEST_2 = {"value": auto()}

            additional_attribute = nonmember({"lorem": "ipsum 1"})

        self.assertEqual(
            {(1, "Test 1"), (2, "Test 2")}, set(TestExtendedChoices.choices)
        )

    def test_absent_value_key_raises_error(self):
        with self.assertRaises(ValueError) as e:

            class TestExtendedChoices(ExtendedChoices, IntegerChoices):
                TEST_1 = {"label": "Test 1"}
                TEST_2 = {"label": "Test 2"}

        self.assertEqual(
            "enum value for TEST_1 should contain member 'value' "
            "when using a dict as value; got TEST_1 = {'label': 'Test 1'}",
            str(e.exception),
        )

    def test_absent_label_computes_default(self):
        class TestExtendedChoices(ExtendedChoices, IntegerChoices):
            TEST_1 = {"value": auto()}
            TEST_2 = auto(), "Autre label"

        self.assertEqual({"Test 1", "Autre label"}, set(TestExtendedChoices.labels))

    def test_absent_additionnal_key_calls_dynamic_attribute_value_method(self):
        class TestExtendedChoices(ExtendedChoices, IntegerChoices):
            TEST_1 = {
                "value": auto(),
                "additionnal_attribute": {"lorem": "ipsum 1"},
            }
            TEST_2 = auto()

            def dynamic_attribute_value(self, name):
                if name == "additionnal_attribute":
                    return {"lorem": "ipsum {}".format(self.value)}
                else:
                    return {"lorem": "ipsum x"}

        self.assertEqual(
            [{"lorem": "ipsum 1"}, {"lorem": "ipsum 2"}],
            [it.additionnal_attribute for it in TestExtendedChoices],
        )

    def test_absent_additionnal_key_no_dynamic_attribute_value_method(self):
        class TestExtendedChoices(ExtendedChoices, IntegerChoices):
            TEST_1 = {
                "value": auto(),
                "additionnal_attribute": {"lorem": "ipsum 1"},
            }
            TEST_2 = auto()

        with self.assertRaises(AttributeError) as e:
            TestExtendedChoices.TEST_2.additionnal_attribute

        self.assertEqual(
            "TestExtendedChoices.TEST_2 does not contain key 'additionnal_attribute'. "
            "Please add key or implement a 'dynamic_attribute_value(self, name)' "
            "method in you enum to provide a value",
            str(e.exception),
        )

    def test_uses_overriden_getter(self):
        class TestExtendedChoices(ExtendedChoices, IntegerChoices):
            TEST_1 = {
                "value": auto(),
                "additionnal_attribute": {"lorem": "ipsum 1"},
            }
            TEST_2 = auto()

            @enum_property
            def additionnal_attribute(self):
                return "overriden attribute"

        self.assertEqual(
            ["overriden attribute", "overriden attribute"],
            [it.additionnal_attribute for it in TestExtendedChoices],
        )

    def test_uses_additional_attribute_private_name(self):
        class TestExtendedChoices(ExtendedChoices, IntegerChoices):
            TEST_1 = {
                "value": auto(),
                "additionnal_attribute_1": {"lorem": "ipsum 1"},
                "additionnal_attribute_2": mark_safe(
                    "<strong>Item 1</strong>"
                ),  # nosec
            }
            TEST_2 = {
                "value": auto(),
                "additionnal_attribute_1": {"lorem": "ipsum 2"},
                "additionnal_attribute_2": mark_safe(
                    "<strong>Item 2</strong>"
                ),  # nosec
            }

            @staticmethod
            def private_variable_name(name):
                return f"m_{name}"

        self.assertEqual(
            {"<strong>Item 1</strong>", "<strong>Item 2</strong>"},
            {it.m_additionnal_attribute_2 for it in TestExtendedChoices},
        )
