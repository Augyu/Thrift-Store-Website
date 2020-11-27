from django.urls import path, re_path
from . import views

app_name = 'users'
urlpatterns = [
    path('register', views.register, name='register'),
    path('profile/<str:username>', views.profile, name='profile'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name="logout"),
]
