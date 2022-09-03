
from django.urls import path
from . import views
urlpatterns = [
    path('hello/', views.index),
    path('registration/', views.register, name='registration'),
    path('login_page/', views.login_f, name='login_page'),
    path('home_page/', views.home, name='home_page'),
    path('profile/', views.profile, name='profile'),
    path('Logout/', views.logo, name='Logout')

]
