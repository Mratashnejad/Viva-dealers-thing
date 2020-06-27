from django.conf.urls import url
from django.urls import path
from . import views


app_name = 'Ecommerce'

urlpatterns = [
    url(r'^$', views.shop_page, name='shop'),
    # path(r'^blackjack/$', views.Blackjack_page, name='Blackjack'),


]
