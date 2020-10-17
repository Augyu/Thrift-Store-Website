from django.urls import path

from . import views

app_name = 'thrifts'
urlpatterns = [
    path('', views.index, name='index'),
    path('user/', views.user, name='user'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name="logout"),
    path('product/', views.list, name='list'),
    path('product/<int:product_id>/', views.detail, name='detail')
]
