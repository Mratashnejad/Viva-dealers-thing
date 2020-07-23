from django.http import HttpResponse
from django.shortcuts import render
from django.conf import settings
from ecommerce.models import Item, UserProfile
from django.views.generic import ListView, DetailView, View


class homepageview(ListView):
    def get_context_data(self, **kwargs):
        context['cat'] = [('Cl', 'Clothes and Uniforms'),
                          ('Ph', 'Phones & Accessories'),
                          ('Je', 'Jewelry & Watches'),
                          ('Ba', 'Bags & Shoes'),
                          ('HA', 'Home Appliance'),
                          ('Be', 'Beauty & Health, Hair'),
                          ('Ap', 'Apartments'),
                          ('Ho', 'Houses')]
        if 'Cl' in request.POST:
            context['items'] = Obj.objects.all.filter(name="Cl")
        if 'Ph' in request.POST:
            context['items'] = Obj.objects.all.filter(name="Ph")
        return render(request, 'index.html', context)


def home_page(request):
    context = {
        'items': Item.objects.all(),
    }
    return render(request, 'index.html', context)


def courses_page(request):
    return render(request, 'courses.html')


def about_page(request):
    return render(request, 'about.html')


def contact_page(request):
    return render(request, 'contact.html')


def blog_page(request):
    return render(request, 'blog.html')


def error404(request, exception):
    return render(request, '404.html')
