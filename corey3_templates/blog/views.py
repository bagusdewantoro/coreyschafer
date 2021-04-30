from django.shortcuts import render
from django.http import HttpResponse

def http_first(request):
    return HttpResponse("<h1>This is HTTP first</h1> \
                        <p>Let's check</p>")

def http_second(request):
    return HttpResponse("<h1>This is HTTP second</h1> \
                        <p>Let's check</p>")

# dummy data 1
raw_posts = [
    {
        'author': 'Bagus',
        'title': 'Post 1',
        'content': 'First Post content',
        'date_post': 'August 27 2021'
    },
    {
        'author': 'User 2',
        'title': 'Post 2',
        'content': 'Second Post content',
        'date_post': 'August 28 2021'
    }
]

def home(request):
    context = {
        'posts': raw_posts
    }
    return render(request, 'blog/home.html', context)

from . import dummy
def about(request):
    dict = {
        'contents': dummy.contents
    }
    return render(request, 'blog/about.html', dict)
