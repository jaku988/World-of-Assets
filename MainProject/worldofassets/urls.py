from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('login_page/', views.user_login, name="user_login"),
    path('registration_page', views.user_registration, name="user_registration"),
    path('user_logout', views.user_logout, name="user_logout")
]