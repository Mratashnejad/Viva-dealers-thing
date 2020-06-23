from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from .forms import RegisterForm
# from django.contrib.auth.forms import UserCreationForm


def Login_page(request):

    return render(request, 'Login_page.html')


def Signup_page(response):
    if response.method == "POST":
        form = RegisterForm(response.POST)
        if form.is_valid():
            form.save()
        return redirect('/home')
    else:
        form = RegisterForm()
    return render(response, 'Signup_page.html', {'form': form})
