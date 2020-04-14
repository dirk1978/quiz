from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('thanks/', views.thanks, name='thanks'),
    path('signup/', views.signup, name='signup'),
    path('signupthanks/', views.signupthanks, name='signupthanks')
]