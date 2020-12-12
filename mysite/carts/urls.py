from django.urls import path, re_path
from . import views

app_name = 'comments'
urlpatterns = [
    path('', views.cart, name='home'),
    path('add', views.add_to_cart, name='add'),
]
