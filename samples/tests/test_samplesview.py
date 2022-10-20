from django.test import RequestFactory, TestCase
from django.core.exceptions import ValidationError

from samples.views import SamplesView


class SamplesViewTestCases(TestCase):

    @classmethod
    def setUpTestData(cls):
        print("\nRunning tests for SamplesView ...\n")
        pass

    def setUp(self) -> None:
        self.response = self.client.get('/samples/', follow=True)

    def test_view_load(self):
        self.assertEqual(self.response.status_code, 200)

    def test_view_content(self):
        self.assertTrue(b'Result of do_lots_of_things is' in self.response.content)

    def test_view_content_has_value(self):
        self.assertTrue(b'1998' in self.response.content)