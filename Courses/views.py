from django.http import HttpResponse
from django.shortcuts import render


def Courses_page(request):
    return render(request, 'index.html')


def Blackjack_page(request):
    return render(request, 'Blackjack.html')


def Poker_page(request):
    return render(request, 'Poker.html')


def Baccarat_page(request):
    return render(request, 'Baccarat.html')


def Keno_page(reqeust):
    return render(reqeust, 'Keno.html')


def Roulatte_page(reuqest):
    return render(reuqest, 'Roulatte.html')


def Dragontiger_page(reuqest):
    return render(reuqest, 'Dragontiger.html')
