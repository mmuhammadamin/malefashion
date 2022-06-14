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


def shop_view(request):
    products = Product.objects.order_by('-id')
    product_image = ProductImage.objects.all()
    cats = Category.objects.all()

    q = request.GET.get('q')
    if q:
        products = products.filter(category_shop__name=q)

    ctx = {
        'products': products,
        'product_image': product_image,
        'cats': cats,

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
