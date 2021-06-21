from django.contrib import admin
from django.urls import path
from login import views

urlpatterns = [
    path("", views.index, name='index'),
    path("home", views.home, name='home'),
    path("login", views.login, name='login'),
    path("signup", views.signup, name='signup'),
    path("upload", views.upload, name='upload'),
    path("gallery", views.gallery, name='gallery'),
    path("contact", views.contact, name='contact'),
]