from django.shortcuts import render, get_object_or_404

# Create your views here.
from .models import Blog


def home(request):

    blogs = Blog.objects
    return render(request, 'blog/news.html', {'allblogs': blogs})


def detail(request, blog_id):

    detail_blog = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'blog/detail.html', {'blog': detail_blog})
