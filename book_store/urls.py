from django.conf.urls import url
from django.urls import path
from book_rent_store import settings
from django.conf.urls.static import static

from . import views

if settings.DEBUG is True:
    urlpatterns = [
                      path('book/<slug>', views.book_view, name='detail'),
                      path('', views.main_view, name='main'),
                      url('book/add_to_cart', views.add_to_cart_view, name='add_to_cart'),
                      url('cart/remove_from_cart', views.remove_from_cart_view, name='remove_from_cart'),
                      path('cart', views.cart_view, name='cart'),
                  ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
