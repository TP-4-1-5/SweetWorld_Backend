from django.urls import path
from . import views

urlpatterns = [
    path('getcommentslist', views.getcommentslist, name='getcommentslist'),
    path('post', views.post, name='post'),
    path('delete', views.delete, name='delete'),
    path('getcomment', views.getcomment, name='getcomment'),
]
