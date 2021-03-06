from django.urls import path
from . import views

app_name = 'orders'
urlpatterns = [
    path('<str:username>/', views.home, name="home"),
    path('add/<int:shopping_cart>', views.add_order, name="add"),
]
