from django.contrib import admin
from django.urls import path
from hmsapp import views

urlpatterns = [
    path('',views.home),
    path('bookorder',views.bookorder),
    path('menucard',views.menucard),
    path('sort/<x>',views.sortfilter),
    path('filprice/<x>',views.filprice),
    path('dash',views.dash),
    path('completed/<rid>',views.completed),
    path('addmenu',views.addmenu),
    path('menu',views.menu),
    path('updatemenu/<rid>',views.updatemenu),
    path('deletemenu/<rid>',views.deletemenu),
    path('catfilter/<cv>',views.catfilter),
    path('orderdone',views.orderdone),
    path('djforms',views.django_form),
    path('register',views.user_register),
    path('login',views.user_login),
    path('static',views.staticfile)
    
]
