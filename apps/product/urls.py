from django.urls import path
from .views import *
app_name='products'
urlpatterns=[
    path('',product_view),
    path('shop/',shop_view),
    path('detail/<int:pk>/', shop_detailed_view, name='detail'),

]
