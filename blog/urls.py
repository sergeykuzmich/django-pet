from django.urls import path

from .views import PostListView, PostView, IndexView, CategoryPostsListView, TagPostsListView, AnalyticsView, \
    PostCreateView, PostEditView

urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path("posts/", PostListView.as_view(), name="post-list"),
    path("posts/create/", PostCreateView.as_view(), name="post-create"),
    path('posts/<int:pk>/edit/', PostEditView.as_view(), name='post-edit'),
    path("posts/<int:pk>/", PostView.as_view(), name="post-detail"),
    path("categories/<int:pk>/posts/", CategoryPostsListView.as_view(), name="category-posts"),
    path("tags/<int:pk>/posts/", TagPostsListView.as_view(), name="tag-posts"),
    path("analytics/", AnalyticsView.as_view(), name="analytics"),
]
