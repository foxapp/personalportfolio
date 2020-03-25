from django.shortcuts import render, get_object_or_404
from django.utils.html import format_html
from .models import Blog


def all_blogs(request):
    # blogs = Blog.objects.all()
    blogs = Blog.objects.order_by('-date')[:5]
    return render(request, 'blog/all_blogs.html', {'blogs':blogs})


def detail(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)
    blog.description = format_html(blog.description)
    # blogs = Blog.objects.all()
    # blogs = Blog.objects.order_by('-date')[:5]
    return render(request, 'blog/detail.html', {'blog': blog})
