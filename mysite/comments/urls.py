from django.urls import path, re_path
from . import views

app_name = 'comments'
urlpatterns = [
    path('add', views.add_comment, name='add'),
    path('edit', views.edit_comment, name='edit'),
    path('delete', views.delete_comment, name='delete'),
]
