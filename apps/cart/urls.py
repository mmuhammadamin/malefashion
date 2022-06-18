from django.urls import path
from .views import add_wishlist,my_wishlist,add_cart,my_cart_view,plus_quantity,minus_quantity,delete_cart_item_view,checkout_view


app_name='carts'

urlpatterns=[
    path('add-wishlist/',add_wishlist,name='add_wishlist'),
    path('wishlist/',my_wishlist,name="my_wishlist"),
    path('add-cart/',add_cart,name="add-cart"),
    path('my-cart/',my_cart_view,name="my_cart"),
    path('minus-quantity/', minus_quantity, name='minus-quantity'),
    path('plus-quantity/', plus_quantity, name='plus-quantity'),
    path('delete-cart-item-view/', delete_cart_item_view, name='delete-cart-item-view'),
    path('checkout/',checkout_view,name='checkout')
]