from django.shortcuts import render
from django.http import HttpResponse

def http_first(request):
    return HttpResponse("<h1>This is HTTP first</h1> \
                        <p>Let's check</p>")

def http_second(request):
    return HttpResponse("<h1>This is HTTP second</h1> \
                        <p>Let's check</p>")
