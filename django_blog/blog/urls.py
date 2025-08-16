from django.urls import path
from .views import (
    PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView
)

urlpatterns = [
    # Home + list
    path("", PostListView.as_view(), name="home"),
    path("posts/", PostListView.as_view(), name="posts"),

    # Create / Read / Update / Delete
    path("posts/new/", PostCreateView.as_view(), name="post-create"),
    path("posts/<int:pk>/", PostDetailView.as_view(), name="post-detail"),
    path("posts/<int:pk>/edit/", PostUpdateView.as_view(), name="post-edit"),
    path("posts/<int:pk>/delete/", PostDeleteView.as_view(), name="post-delete"),
]
# post/<int:pk>/delete/", "post/<int:pk>/update/", "post/new/
