from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', views.PostlistView.as_view() ,name='home'),
    path('register/', views.register ,name='register'),
    path('login/',auth_views.LoginView.as_view(template_name='blog/login.html'),name='login'),
    path('logout/',auth_views.LogoutView.as_view(template_name='blog/logout.html'),name='logout'),
    path('profile/',views.profile, name='profile'),
    path('about/',views.about, name='about'),
]