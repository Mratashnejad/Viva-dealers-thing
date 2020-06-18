from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls import url, include
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^$', views.home_page, name='homepage'),
    url(r'^courses/$', views.courses_page, name='courses'),
    url(r'^about/$', views.about_page, name='about'),
    url(r'^contact/$', views.contact_page, name='contact'),
    url(r'^blog/$', views.blog_page, name='blog'),
    url(r'^courses/', include('Courses.urls')),
    url(r'^accounts/', include('Accounts.urls')),
]

handler404 = views.error404
urlpatterns += staticfiles_urlpatterns()
