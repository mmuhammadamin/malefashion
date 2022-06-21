from django.core.paginator import Paginator
from django.shortcuts import render

from apps.blog.models import Post
from .models import Category, ProductImage, Category_name, Product
from ..cart.models import Cart


def product_view(request):
    product = Product.objects.order_by('-id')[:8]
    blogs = Post.objects.order_by('id')[0:3]
    categories = Category.objects.all()
    product_image = ProductImage.objects.all()
    categories_name = Category_name.objects.all()

    ctx = {
        'product': product,
        'blogs': blogs,
        'categories': categories,
        'product_image': product_image,
        'categories_name': categories_name,

    }
    return render(request, 'index.html', ctx)




def shop_view(request):
    products = Product.objects.order_by('-id')
    w = request.GET.get('search')
    q = request.GET.get('q')
    s=request.GET.get('s')

    if w:
        products = products.filter(name__icontains=w)
    if q:
        products = products.filter(category_shop__name__iexact=q)
    if s:
        products = products.filter(category_shop__name__icontains=s)

    product_image = ProductImage.objects.all()
    cats = Category.objects.all()
    p = Paginator(products, 6)
    page = request.GET.get('page')
    price_filter_id = request.GET.get('filter_price')

    product = p.get_page(page)
    list = []

    for page in range(1, product.paginator.num_pages + 1):
        list.append(page)


    if price_filter_id:
        product = Product.objects.filter(category__product__price=price_filter_id)


    ctx = {
        'products': products,
        'product_image': product_image,
        'cats': cats,
        'product': product,
        'list': list,
        'p': p

    }
    return render(request, 'shop.html', ctx)


def shop_detailed_view(request, pk):
    products = Product.objects.order_by('-id')
    product = Product.objects.get(id=pk)
    last_products = Product.objects.order_by('category_shop')[0:4]
    cart, cart = Cart.objects.get_or_create(client=request.user, is_ordered=False)


    ctx = {
        'products': products,
        'product': product,
        'last_products': last_products,
        'cart':cart
    }

    return render(request, 'shop-details.html', ctx)

# Create your views here.



