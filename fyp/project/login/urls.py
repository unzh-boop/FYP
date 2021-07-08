from django.contrib import admin
from django.urls import path
from login import views
from django.views.static import serve
from django.conf.urls import url


urlpatterns = [
    path("", views.index, name='index'),
    path("home", views.home, name='home'),
    path("login", views.login, name='login'),
    path("signup", views.signup, name='signup'),
    path("upload", views.upload, name='upload'),
    path("gallery", views.gallery, name='gallery'),
    path("contact", views.contact, name='contact'),
    url(r'^media/(?P<path>.*)$', serve,{'document_root':       settings.MEDIA_ROOT}), 
    url(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}), 
]