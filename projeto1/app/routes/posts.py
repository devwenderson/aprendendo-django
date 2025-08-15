from django.urls import path
from app.views.posts import PostsPageView

urlpatterns = [
    path("posts/", PostsPageView.as_view(), name="posts-list")
]