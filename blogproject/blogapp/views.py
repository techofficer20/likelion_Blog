from django.shortcuts import render, get_object_or_404
from .models import Blog
# Create your views here.

def index(request):
    blog = Blog.objects
    return render(request, 'index.html', {'blog' : blog})

def detail(request, blog_id):
    blog_detail = get_object_or_404(Blog, pk = blog_id)
    return render(request, 'detail.html', {'blog_detail' : blog_detail})