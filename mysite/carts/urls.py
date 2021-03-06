from django.urls import path, re_path
from . import views

app_name = 'carts'
urlpatterns = [
    path('', views.cart, name='home'),
    path('add', views.add_to_cart, name='add'),
    path('delete/<int:shopping_cart>/<int:product>',
         views.delete_from_cart, name='delete'),
]
