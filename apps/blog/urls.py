from django.urls import path
from .views import blog_detail,blog_list,about


app_name='blog'

urlpatterns=[
    path('', blog_list, name='list'),

    path('detail/<int:pk>/', blog_detail, name='detail'),

    path('about/',about,name='about')


]
