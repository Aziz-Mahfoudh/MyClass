from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.login),
    path('toLogin/', views.toLogin, name="toLogin"),
    path('logout/', views.logout, name="logout"),
    path('home/', views.home),
]