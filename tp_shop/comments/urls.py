from django.urls import path
from . import views
from .views import CommentListView, CreateCommentView, DeleteCommentView, CommentView

urlpatterns = [
    path('getcommentslist', CommentListView.as_view(), name='getcommentslist'),
    path('getcomment', CommentView.as_view(), name='getcomment'),
    path('post', CreateCommentView.as_view(), name='post'),
    path('delete', DeleteCommentView.as_view(), name='delete'),
]