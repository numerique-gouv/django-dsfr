from http import HTTPStatus

from django.test import TestCase
from django.urls import reverse


class DsfrBaseForm(TestCase):
    sample_data = {"user_name": "Example Name", "sample_number": 5, "sample_json": "{}"}

    def test_valid_form(self):
        response = self.client.post(
            reverse("page_form"),
            data=self.sample_data,
        )

        self.assertEqual(response.status_code, HTTPStatus.OK)

    def test_form_sets_autofocus_on_first_error(self):
        sample_data = self.sample_data
        sample_data["sample_number"] = -5
        response = self.client.post(
            reverse("page_form"),
            data=sample_data,
        )

        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertContains(
            response,
            """<input type="number" name="sample_number" value="-5"
            aria-invalid="true" aria-describedby="id_sample_number-desc-error" class="fr-input"
            autofocus="" required id="id_sample_number">""",
            html=True,
        )
        self.assertContains(response, "Merci d’entrer un nombre positif", html=True)
