from django.urls import path, re_path
from . import views

app_name = 'users'
urlpatterns = [
    path('', views.list, name='list'),
    path('register', views.register, name='register'),
    path('role', views.change_role, name="change_role"),
    path('profile/<str:username>', views.profile, name='profile'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name="logout"),
]
