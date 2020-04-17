from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('thanks/', views.thanks, name='thanks'),
    path('signup/', views.signup, name='signup'),
    path('send_bingo_links/', views.send_bingo_links, name='send_bingo_links'),
    path('signupthanks/', views.signupthanks, name='signupthanks'),
    path('leaderboard/', views.leaderboard, name='leaderboard')
]