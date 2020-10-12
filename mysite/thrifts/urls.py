from django.urls import path

from . import views

app_name = 'thrifts'
urlpatterns = [
    path('', views.index, name='index'),
    path('list/', views.list, name='list'),
    path('detail/', views.detail, name='detail')
]
