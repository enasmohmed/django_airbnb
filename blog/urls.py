from django.urls import path
from . import views
from .views import PostList, PostDetail, PostByCategory, PostByTags

app_name = 'blog'

urlpatterns = [
    path("", PostList.as_view(), name="post_list"),
    path("<slug:slug>", PostDetail.as_view(), name="post_detail"),

    path("category/<str:slug>", PostByCategory.as_view(), name="post_by_category"),
    path("tags/<slug:slug>", PostByTags.as_view(), name="post_by_tags"),
]
