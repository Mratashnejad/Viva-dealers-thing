from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls import url, include
from django.urls import path
from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home_page , name='homepage'),
    path('courses/', include('Courses.urls'), name='Courses'),
    path('games/', include('Games.urls'), name='Games'),
    path('shop/', include('ecommerce.urls'), name='ecommerce'),
    url(r'^about/$', views.about_page, name='about'),
    url(r'^contact/$', views.contact_page, name='contact'),
    url(r'^blog/$', views.blog_page, name='blog'),
    path('accounts/', include('allauth.urls')),
]

handler404 = views.error404
urlpatterns += staticfiles_urlpatterns()


if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [path('__debug__/', include(debug_toolbar.urls))]
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
