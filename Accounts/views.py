from django.http import HttpResponse
from django.shortcuts import render
# from django.contrib.auth.forms import UserCreationForm


def Login_page(request):
    return render(request, 'Login_page.html')


def Signup_page(request):
    # form = UserCreationForm()
    return render(request, 'Signup_page.html')
