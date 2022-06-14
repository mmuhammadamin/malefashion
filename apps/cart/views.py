from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render

from apps.product.models import Product, Category
from .models import WishList


# Create your views here.
def add_wishlist(request):
    pid = request.GET.get('_pid')
    user = request.user
    product = Product.objects.get(id=pid)
    wishlist_count = WishList.objects.filter(user=user, product=product).count()
    if wishlist_count < 1:

        wishlist = WishList.objects.create(user=user, product=product)

        data = {
            'success': True,
            'product': product.name
        }


    else:
        data = {
            'success': False,
            'error_message': 'Already in ur wishlist',
            'product': product.name
        }
    return JsonResponse(data)


@login_required(login_url='/accounts/login/')
def my_wishlist(request):
    my_wishlist = WishList.objects.filter(user=request.user)
    cats = Category.objects.all()
    q = request.GET.get('q')
    if q:
        my_wishlist = my_wishlist.filter(product__category_shop__name__exact=q)
    ctx = {
        'products': my_wishlist,
        'cats': cats,
    }

    return render(request, 'my-wishlist.html', ctx)
