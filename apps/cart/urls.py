from django.urls import path
from .views import add_wishlist,my_wishlist,add_cart


app_name='carts'

urlpatterns=[
    path('add-wishlist/',add_wishlist,name='add_wishlist'),
    path('wishlist/',my_wishlist,name="my_wishlist"),
    path('add-cart/',add_cart,name="add-cart")
]