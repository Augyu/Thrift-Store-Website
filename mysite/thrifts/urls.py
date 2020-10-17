from django.urls import path

from . import views

app_name = 'thrifts'
urlpatterns = [
    path('', views.index, name='index'),
    path('home/', views.home, name='home'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name="logout"),
    path('product/', views.list, name='list'),
    path('product/<int:product_id>/', views.detail, name='detail'),
    path('sell/', views.sell, name='sell')
]
