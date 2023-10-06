from django.urls import path
from . import views
from .views import Download

urlpatterns = [
    path('', views.nothome),
    path('nothome', views.nothome),
    path('nothome/', views.nothome),

    path('affiche/', Download.as_view(template_name="propterre/affiche.html")),
    path('affiche/deleteimg/<int:id>', Download.as_view()),

    path("home/admin", views.register),
    path("login_user", views.login_user),
    path("logout_user", views.logout_user),
    path("home/login_user", views.login_user),
    path("home/logout_user", views.logout_user),

    path('home', views.home),
    path('home/', views.home),
    
    path('profil/<int:id>/',views.profil),
    path('propterre/profil/<int:id>/',views.profil),
    path('home/admin/delete/<int:id>/', views.delete),
    path('home/admin/deleteins/<int:id>/', views.deleteins),
    path('home/admin/deletesig/<int:id>/', views.deletesig),
    path('home/admin/deleteuser/<str:username>/', views.deleteuser),
    path('traitement/', views.traitement),
    path('traitementins/', views.traitementins),
    path('traitementsig/', views.traitementsig),

    path('films',views.films),
    path('films/',views.films),

    path('series',views.series),
    path('series/',views.series),


]
