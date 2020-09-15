from django.db import models
from django.urls import reverse
from django.utils.text import slugify


class BookType(models.Model):
    type_name = models.CharField(max_length=100, default="regular")
    type_price = models.DecimalField(max_digits=9, decimal_places=2, default=1.5)

    def __str__(self):
        return self.type_name


class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    slug = models.SlugField(editable=False, unique=True)
    image = models.ImageField(upload_to='media/book_store', blank=True)
    book_type = models.ForeignKey(BookType, on_delete=models.CASCADE, null=True, blank=True)

    def get_absolute_url(self):
        return reverse('detail', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        self.slug = '-'.join((slugify(self.title), slugify(self.author)))
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.author} {self.title}"


class RentedBook(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    rent_days = models.PositiveSmallIntegerField()

    def get_item_total(self):
        return self.book.book_type.type_price * self.rent_days

    def __str__(self):
        return f"Rented book: {self.book.title} for {self.rent_days} day(s)"


class Cart(models.Model):
    items = models.ManyToManyField(RentedBook, blank=True)
    cart_total = models.DecimalField(max_digits=9, decimal_places=2, default=0.00)

    def add_to_cart(self, item_slug, rent_days):
        cart = self
        book = Book.objects.get(slug=item_slug)
        new_item, _ = RentedBook.objects.get_or_create(book=book, rent_days=rent_days)
        if len(cart.items.all()) > 0:
            for item in cart.items.all():
                if item.book == book:
                    cart.items.remove(item)
                    cart.items.add(new_item)
            cart.items.add(new_item)
        else:
            cart.items.add(new_item)

        cart.update_total_price()
        cart.save()

    def remove_from_cart(self, item_slug):
        cart = self
        book = Book.objects.get(slug=item_slug)
        for cart_item in cart.items.all():
            if cart_item.book == book:
                cart.items.remove(cart_item)
                cart.update_total_price()
                cart.save()

    def update_total_price(self):
        cart = self
        new_cart_total = 0.0
        for item in cart.items.all():
            new_cart_total += float(item.get_item_total())
        cart.cart_total = new_cart_total
