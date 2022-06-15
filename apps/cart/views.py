from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.http import JsonResponse
from django.shortcuts import render

from apps.product.models import Product, Category
from .models import WishList, Cart, CartItem


# Create your views here.
def add_wishlist(request):
    pid = request.GET.get('_pid')
    user = request.user
    product = Product.objects.get(id=pid)
    wishlist_count = WishList.objects.filter(user=user, product=product).count()
    if wishlist_count < 1:
        WishList.objects.create(user=user, product=product)

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
    p = Paginator(WishList.objects.all().order_by('-id').filter(user=request.user), 6)
    page = request.GET.get('page')
    product = p.get_page(page)
    list = []

    for page in range(1, product.paginator.num_pages + 1):
        list.append(page)
    q = request.GET.get('q')
    w = request.GET.get('search')
    if q:
        product = my_wishlist.filter(product__category_shop__name__exact=q)
    if w:
        product = my_wishlist.filter(product__name__iexact=w)
    ctx = {
        'products': my_wishlist,
        'cats': cats,

        'product': product,
        'list': list,
        'p': p
    }

    return render(request, 'my-wishlist.html', ctx)


def add_cart(request):
    pid = request.GET.get('_pid')
    user = request.user
    product = Product.objects.get(id=pid)
    my_cart, new_cart = Cart.objects.get_or_create(client=user, is_ordered=False)
    data = None
    if my_cart:
        CartItem.objects.create(product=product, cart=my_cart)
        data = {
            'success': True,
            'product': product.name

        }

    if new_cart:
        CartItem.objects.create(product=product, cart=new_cart)
        data = {
            'success': True,
            'product': product.name

        }
    return JsonResponse(data, status=201)
