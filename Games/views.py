from django.http import HttpResponse
from django.shortcuts import render
from Games import Game_Class


def blackjack_game(request):
    # context  = 
        
    return render(request, 'BLJC.html' , context)
