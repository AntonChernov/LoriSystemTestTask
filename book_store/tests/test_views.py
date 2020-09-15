from django.test import TestCase

from book_store.models import (Book,
                               RentedBook,
                               Cart)


class ViewsTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Cart.objects.create()
        Book.objects.create(title="Harry Potter", author="J.K. Rowling", description="Simple description")
        Book.objects.create(title="Hunger Games", author="S. Collins",
                            description="Book about hunger games")

    def test_main_page_view(self):
        response = self.client.get('/')
        self.assertEquals(200, response.status_code)
        self.assertEquals(2, response.context['books'].count())

    def test_book_view(self):
        book = Book.objects.get(id=1)
        response = self.client.get(f'/book/{book.slug}')
        self.assertEquals(200, response.status_code)
        book = response.context['book']

        self.assertEquals('J.K. Rowling', book.author)
        self.assertEquals('Harry Potter', book.title)
        self.assertEquals('harry-potter-jk-rowling', book.slug)

    def test_cart_view(self):
        response = self.client.get('/cart')
        self.assertEquals(200, response.status_code)
