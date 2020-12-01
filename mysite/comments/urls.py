from django.urls import path, re_path
from . import views

app_name = 'comments'
urlpatterns = [
    path('add', views.add_comment, name='add'),
    # path('<int:comment_id>/edit', views.edit_comment, name='edit'),
    # path('<int:comment_id>/delete', views.delete, name='delete'),
]
