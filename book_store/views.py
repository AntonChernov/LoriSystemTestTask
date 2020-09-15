from django.shortcuts import render, redirect

from book_store.models import Book
from book_store.utils import get_cart
from book_store.forms import AddToCartForm


def main_view(request):
    cart = get_cart(request)
    books = Book.objects.all()
    return render(request, 'book_store/homepage.html', {'books': books, 'cart': cart})


def book_view(request, slug):
    cart = get_cart(request)
    book = Book.objects.get(slug=slug)
    form = AddToCartForm(initial={'item_slug': slug})

    return render(request, 'book_store/details.html', {'book': book, 'cart': cart, 'form': form})


def cart_view(request):
    cart = get_cart(request)
    return render(request, 'book_store/cart.html', {'cart': cart})


def add_to_cart_view(request):
    cart = get_cart(request)
    form = AddToCartForm(request.POST or None)
    if form.is_valid():
        item_slug = form.cleaned_data['item_slug']
        rent_days = form.cleaned_data['rent_days']
        cart.add_to_cart(item_slug, rent_days)
        return redirect('detail', item_slug)


def remove_from_cart_view(request):
    if 'remove_from_cart' in request.POST:
        cart = get_cart(request)
        book_slug = request.POST['remove_from_cart']
        cart.remove_from_cart(book_slug)
    return redirect('cart')
