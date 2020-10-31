from django.urls import path, re_path
from . import views

app_name = 'thrifts'
urlpatterns = [
    path('', views.home, name='home'),
    path('home/', views.home, name='home'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name="logout"),
    path('product/', views.list, name='list'),
    path('product/<int:product_id>/', views.detail, name='detail'),
    path('product/<int:product_id>/edit', views.edit, name='edit'),
    path('product/<int:product_id>/delete', views.delete, name='delete'),
    path('sell/', views.sell, name='sell'),
    path('seller/<seller>/', views.seller, name="seller"),
    path('seller/<seller>/comment', views.leave_comment, name="comment"),
    path('seller/<seller>/num_of_comment',
         views.get_num_of_comment, name="numOfComment")
]
