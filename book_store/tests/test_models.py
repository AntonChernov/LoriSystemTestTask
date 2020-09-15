from django.test import TestCase

from book_store.models import (Book,
                               BookType,
                               RentedBook,
                               Cart)


class BookModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        Book.objects.create(title="Harry Potter", author="J.K. Rowling", description="Simple description")

    def test_title_label(self):
        book = Book.objects.get(id=1)
        field_label = book._meta.get_field('title').verbose_name
        self.assertEquals(field_label, 'title')

    def test_slug_field(self):
        book = Book.objects.get(id=1)
        slug_field = book.slug
        self.assertEquals(slug_field, 'harry-potter-jk-rowling')

    def test_object_name_is_author_and_title(self):
        book = Book.objects.get(id=1)
        expected_object_name = f'{book.author} {book.title}'
        self.assertEquals(expected_object_name, str(book))


class RentedBookTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        fiction_type = BookType.objects.create(type_name="fiction", type_price=3)
        book = Book.objects.create(title="Harry Potter", author="J.K. Rowling",
                                   description="Simple description",
                                   book_type=fiction_type)
        RentedBook.objects.create(book=book, rent_days=5)

    def test_get_item_total(self):
        rented_book = RentedBook.objects.get(id=1)
        self.assertEquals(rented_book.get_item_total(), 15)

    def test_object_name_is_title_and_rent_days(self):
        rented_book = RentedBook.objects.get(id=1)
        expected_object_name = f"Rented book: {rented_book.book.title} for {rented_book.rent_days} day(s)"
        self.assertEquals(expected_object_name, str(rented_book))


class CartTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        regular_type = BookType.objects.create(type_name="regular", type_price=1.5)
        fiction_type = BookType.objects.create(type_name="fiction", type_price=3)
        first_book = Book.objects.create(title="Harry Potter", author="J.K. Rowling",
                                         description="Simple description",
                                         book_type=regular_type)
        second_book = Book.objects.create(title="Hunger Games", author="S. Collins",
                                          description="Book about hunger games",
                                          book_type=fiction_type)
        RentedBook.objects.create(book=first_book, rent_days=5)
        RentedBook.objects.create(book=second_book, rent_days=7)

        Cart.objects.create()

    def test_add_to_cart(self):
        first_rented_book = RentedBook.objects.get(id=1)
        second_rented_book = RentedBook.objects.get(id=2)
        cart = Cart.objects.get(id=1)
        self.assertEquals(0, cart.cart_total)
        self.assertEquals(0, len(cart.items.all()))
        cart.add_to_cart(first_rented_book.book.slug, first_rented_book.rent_days)
        self.assertEquals(7.5, cart.cart_total)
        cart.add_to_cart(second_rented_book.book.slug, second_rented_book.rent_days)
        self.assertEquals(28.5, cart.cart_total)
        self.assertEquals(2, len(cart.items.all()))

    def test_remove_from_cart(self):
        first_rented_book = RentedBook.objects.get(id=1)
        second_rented_book = RentedBook.objects.get(id=2)
        cart = Cart.objects.get(id=1)
        cart.add_to_cart(first_rented_book.book.slug, first_rented_book.rent_days)
        self.assertEquals(7.5, cart.cart_total)
        cart.add_to_cart(second_rented_book.book.slug, second_rented_book.rent_days)
        self.assertEquals(28.5, cart.cart_total)
        cart.remove_from_cart(first_rented_book.book.slug)
        self.assertEquals(21, cart.cart_total)
        self.assertEquals(1, len(cart.items.all()))
        cart.remove_from_cart(second_rented_book.book.slug)
        self.assertEquals(0, cart.cart_total)
        self.assertEquals(0, len(cart.items.all()))

    def test_update_total_price(self):
        first_rented_book = RentedBook.objects.get(id=1)
        cart = Cart.objects.get(id=1)
        self.assertEquals(0, len(cart.items.all()))
        cart.items.add(first_rented_book)
        self.assertEquals(1, len(cart.items.all()))
        self.assertEquals(0, cart.cart_total)
        cart.update_total_price()
        self.assertNotEquals(0, cart.cart_total)
        self.assertEquals(7.5, cart.cart_total)
