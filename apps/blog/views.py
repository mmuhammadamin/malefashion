from django.shortcuts import render

from .models import Post, Tag


# Create your views here.


# Create your views here.
def blog_list(request):

    blogs = Post.objects.order_by('-id')[:9]

    ctx = {
        'blogs': blogs,
    }
    return render(request, 'blog.html', ctx)


def blog_detail(request,pk):
    blogs = Post.objects.order_by('-id')
    blog = Post.objects.get(id=pk)

    tag = Tag.objects.all()

    ctx = {
        'blogs': blogs,
        'tag': tag,
        'blog': blog,

    }
    try:
        prev = Post.objects.get(id=pk-1)
        ctx['prev'] = prev
    except:
        pass
    try:
        next = Post.objects.get(id=pk+1)
        ctx['next'] = next
    except:
        pass

    return render(request, 'blog-details.html', ctx)

def about(request):
    return render(request,'about.html')