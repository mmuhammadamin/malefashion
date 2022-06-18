from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.http import JsonResponse
from django.shortcuts import render, redirect

from apps.product.models import Product, Category
from .forms import OrderForm
from .models import WishList, Cart, CartItem


# Create your views here.
def add_wishlist(request):
    pid = request.GET.get('_pid')
    user = request.user
    product = Product.objects.get(id=pid)
    wishlist_count = WishList.objects.filter(user=user, product=product).count()
    print(wishlist_count)
    if wishlist_count < 1:
        WishList.objects.create(user=user, product=product)

        data = {
            'success': True,
            'product': product.name
        }

    else:
        WishList.objects.get(user=user, product=product).delete()

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


def my_cart_view(request):
    cart, cart = Cart.objects.get_or_create(client=request.user, is_ordered=False)
    ctx = {
        'cart': cart
    }

    return render(request, 'shopping-cart.html', ctx)


def plus_quantity(request):
    ciid = request.GET.get('_ciid')

    cart_item = CartItem.objects.get(id=ciid)
    cart_item.quantity += 1
    cart_item.save()
    data = {
        'success': True,
        'message': 'Cart item incremented by one',
        'cart_item': cart_item.get_total
    }
    return JsonResponse(data, status=200)


def minus_quantity(request):
    ciid = request.GET.get('_ciid')
    cart_item = CartItem.objects.get(id=ciid)
    if cart_item.quantity > 1:
        cart_item.quantity -= 1
        cart_item.save()
        data = {
            'success': True,
            'message': 'Cart item decremented by one'
        }
    else:
        cart_item.delete()
        data = {
            'success': True,
            'deleted': True,
            'message': 'Cart item deleted'
        }

    return JsonResponse(data, status=200)


def delete_cart_item_view(request):
    ciid = request.GET.get('_ciid')
    cart_item = CartItem.objects.get(id=ciid)

    cart_item.delete()
    data = {
        'success': True,
        'message': 'Cart item deleted',
        'deleted': True
    }

    return JsonResponse(data, status=200)


def checkout_view(request):
    categories = Category.objects.all()
    cart_id = request.GET.get('cart_id')
    cart = Cart.objects.filter(id=cart_id).first()
    form = OrderForm()
    is_ordered = False
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.cart = cart
            order.client = request.user
            order.save()
            cart.is_ordered = True
            cart.save()
            is_ordered = True

            return redirect('.')
    ctx = {
        'form': form,
        'is_ordered': is_ordered,
    }
    return render(request, 'checkout.html', ctx)
