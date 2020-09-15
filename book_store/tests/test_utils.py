from django.test import TestCase
from book_store import utils


class UtilsTest(TestCase):

    def test_get_cart_method(self):
        response = self.client.get('/')

        self.assertEquals(response.status_code, 200)
        self.assertEquals(1, utils.get_cart(self.client).id)
