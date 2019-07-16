from django.shortcuts import render
from .models import Blog
# Create your views here.

def index(request):
    blog = Blog.objects
    return render(request, 'index.html', {'blog' : blog})