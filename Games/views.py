from django.http import HttpResponse
from django.shortcuts import render


def blackjack_game(request):
    return render(request, 'BLJC.html')
