from django.urls import path
from . import views

urlpatterns = [
    path('first/', views.http_first, name='http-first'),
    path('second/', views.http_second, name='http-second'),
    
]
