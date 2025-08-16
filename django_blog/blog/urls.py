# blog/urls.py
from django.urls import path
from .views import (
    PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView,
    add_comment, CommentUpdateView, CommentDeleteView
)

urlpatterns = [
    path("", PostListView.as_view(), name="home"),
    path("posts/", PostListView.as_view(), name="posts"),
    path("posts/new/", PostCreateView.as_view(), name="post-create"),
    path("posts/<int:pk>/", PostDetailView.as_view(), name="post-detail"),
    path("posts/<int:pk>/edit/", PostUpdateView.as_view(), name="post-edit"),
    path("posts/<int:pk>/delete/", PostDeleteView.as_view(), name="post-delete"),

    # comments
    path("posts/<int:pk>/comments/new/", add_comment, name="comment-add"),
    path("comments/<int:pk>/edit/", CommentUpdateView.as_view(), name="comment-edit"),
    path("comments/<int:pk>/delete/", CommentDeleteView.as_view(), name="comment-delete"),
]
# post/<int:pk>/delete/", "post/<int:pk>/update/", "post/new/
