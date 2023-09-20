from django.urls import path
from . import views

urlpatterns = [

    path('', views.index),
    path('nggyu', views.nggyu),
    path('old', views.old),


    path('streamingpower/', views.nothome),
    path('streamingpower', views.nothome),

    path("streamingpower/home/admin", views.register),
    path("streamingpower/login_user", views.login_user),
    path("streamingpower/logout_user", views.logout_user),
    path("streamingpower/home/login_user", views.login_user),
    path("streamingpower/home/logout_user", views.logout_user),

    path('streamingpower/home', views.home),
    path('streamingpower/home/', views.home),

    path('streamingpower/update/<int:id>/',views.update),
    path('streamingpower/propterre/update/<int:id>/',views.update),
    path('streamingpower/home/admin/delete/<int:id>/', views.delete),
    path('streamingpower/home/admin/deleteuser/<str:username>/', views.deleteuser),
    path('streamingpower/propterre/traitement/', views.traitement),

    path('streamingpower/films',views.films),
    path('streamingpower/films/',views.films),

    path('streamingpower/series',views.series),
    path('streamingpower/series/',views.series),


]
