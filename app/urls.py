from django.urls import path
from . import views

urlpatterns = [
    path('', views.nothome),
    path('nothome', views.nothome),
    path('nothome/', views.nothome),

    path("affiche/", views.affiche),

    path("home/admin", views.register),
    path("login_user", views.login_user),
    path("logout_user", views.logout_user),
    path("home/login_user", views.login_user),
    path("home/logout_user", views.logout_user),

    path('home', views.home),
    path('home/', views.home),

    path('update/<int:id>/',views.update),
    path('propterre/update/<int:id>/',views.update),
    path('home/admin/delete/<int:id>/', views.delete),
    path('home/admin/deleteuser/<str:username>/', views.deleteuser),
    path('traitement/', views.traitement),

    path('films',views.films),
    path('films/',views.films),

    path('series',views.series),
    path('series/',views.series),


]
