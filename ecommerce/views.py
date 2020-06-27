from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required


def shop_page(request):
    return render(request, 'index.html')
