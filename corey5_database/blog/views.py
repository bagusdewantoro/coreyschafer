from django.shortcuts import render
from .models import Post

def home(request):
    PostAll = Post.objects.all()
    return render(request, 'blog/home.html', {'posts': PostAll})

from . import dummy
def about(request):
    return render(request, 'blog/about.html', {'contents': dummy.contents})
