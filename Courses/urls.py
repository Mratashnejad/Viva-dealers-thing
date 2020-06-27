from django.conf.urls import url
from django.urls import path
from . import views


app_name = 'Courses'

urlpatterns = [
    url(r'^$', views.Courses_page, name='Courses'),
    url(r'^blackjack/$', views.Blackjack_page, name='Blackjack'),
    url(r'^poker/$', views.Poker_page, name='Poker'),
    url(r'^roulatte/$', views.Roulatte_page, name='Roulatte'),
    url(r'^baccarat/$', views.Baccarat_page, name='Baccarat'),
    url(r'^kenno/$', views.Keno_page, name='Keno'),
    url(r'^dragontiger/$', views.Dragontiger_page, name='Dragontiger'),


]
