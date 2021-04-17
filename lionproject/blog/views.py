from django.shortcuts import render, get_object_or_404
from .models import Blog
# Create your views here.

def home(request):
    data = Blog.objects.all()
    return render(request, 'home.html', {'data':data})

def detail(request, id):
    blog = get_object_or_404(Blog, pk = id)
    return render(request, 'detail.html', {'blog':blog})