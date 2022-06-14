from .views import contact_view
from django.urls import path

app_name='contact'

urlpatterns=[
    path('', contact_view, name='contact'),




]
