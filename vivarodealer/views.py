from django.http import HttpResponse
from django.shortcuts import render
from django.conf import settings

def home_page(request):
    return render(request, 'index.html')


def courses_page(request):
    return render(request, 'courses.html')


def about_page(request):
    return render(request, 'about.html')


def contact_page(request):
    return render(request, 'contact.html')


def blog_page(request):
    return render(request, 'blog.html')

def error404(request , exception):
      return render(request, '404.html')
     
