from django.conf.urls import url
from django.urls import path
from . import views


app_name = 'Ecommerce'

urlpatterns = [
    url(r'^$', views.shop_page, name='shop_page'),
    url(r'^product/$', views.shop_page, name='product'),
    # path(r'^blackjack/$', views.Blackjack_page, name='Blackjack'),


]

