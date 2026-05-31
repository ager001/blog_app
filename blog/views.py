from django.shortcuts import render
from .models import Post


posts = [
    {
        'author': 'John Doe',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'created_at': 'August 27, 2024'
    },
    {
        'author': 'Jane Doe',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'created_at': 'August 28, 2024'
    }
]

def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html')
