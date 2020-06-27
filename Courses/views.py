from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required


def Courses_page(request):
    return render(request, 'index.html')

# login required to access the courses data using @decoreators


@login_required(login_url="/accounts/login/")
def Blackjack_page(request):
    return render(request, 'Blackjack.html')


@login_required(login_url="/accounts/login/")
def Poker_page(request):
    return render(request, 'Poker.html')


@login_required(login_url="/accounts/login/")
def Baccarat_page(request):
    return render(request, 'Baccarat.html')


@login_required(login_url="/accounts/login/")
def Keno_page(reqeust):
    return render(reqeust, 'Keno.html')


@login_required(login_url="/accounts/login/")
def Roulatte_page(reuqest):
    return render(reuqest, 'Roulatte.html')


@login_required(login_url="/accounts/login/")
def Dragontiger_page(reuqest):
    return render(reuqest, 'Dragontiger.html')
