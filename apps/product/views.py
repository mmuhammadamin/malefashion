from django.core.paginator import Paginator
from django.shortcuts import render

from apps.blog.models import Post
from .models import Category, Product, ProductImage, Category_name


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
        'categories_name': categories_name

    }
    return render(request, 'index.html', ctx)


# def base_view(request):
#     product = Product.objects.order_by('-id')[:8]
#
#     search_result = Product.objects.all().order_by('-id')
#     result = request.GET.get('search')
#
#     if result:
#         product = search_result.filter(title__icontains=result)
#
#     ctx={
#         'post':product
#     }
#
#     return render(request, 'base.html',ctx)


def shop_view(request):
    products = Product.objects.order_by('-id')
    product_image = ProductImage.objects.all()
    cats = Category.objects.all()
    p = Paginator(Product.objects.all().order_by('-id'), 6)
    page = request.GET.get('page')
    price_filter_id = request.GET.get('filter_price')

    product = p.get_page(page)
    list = []

    for page in range(1, product.paginator.num_pages + 1):
        list.append(page)

    q = request.GET.get('q')
    w = request.GET.get('search')

    if price_filter_id:
        product = Product.objects.filter(category__product__price=price_filter_id)

    if q:
        product = products.filter(category_shop__name=q)
    if w:
        product = products.filter(category__product__name=w)

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

    ctx = {
        'products': products,
        'product': product,
        'last_products': last_products
    }

    return render(request, 'shop-details.html', ctx)

# Create your views here.
