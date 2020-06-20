from django.conf.urls import url
from django.urls import path
from . import views



app_name = 'Games'
urlpatterns = [
    url(r'^g/$', views.blackjack_game, name='blackjackgame'),
    
]