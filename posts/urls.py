# from django.contrib import admin
from django.urls import path
from posts import views
from .views import *


urlpatterns = [
    path('index', views.index, name = "index"),
    path('about/', views.about, name = "about"),
    path('index.html', views.index, name="index"),
    path('about.html', views.about, name="about"),
    path('nurs', views.nurs, name = "nurs"),
    path('register', views.register, name = "register"),
    path('someinfo', views.someinfo, name = "someinfo"),
    path('nurs.html', views.nurs, name = "nurs"),
    path('register.html', views.register, name = "register"),
    path('someinfo.html', views.someinfo, name = "someinfo"),
    path('contactus', views.contact, name = "contactus"),
    path('mainpage', views.mainpage, name = "mainpage"),
    path('contactus.html', views.contact, name="contactus"),
    path('mainpage.html', views.mainpage, name="mainpage"),
    path('home', views.home, name = "home"),
    path('post/<slug:post_slug>', views.show_post, name='post'),
    path('home.html', views.home, name = "home"),
    path('u_comment', views.u_comment, name = "u_comment"),
    path('u_comment.html', views.u_comment, name = "u_comment"),
    path('registration/', createuser, name="create_user"),
    path('main_site/', views.bonus_main, name="Tempsoft"),
]