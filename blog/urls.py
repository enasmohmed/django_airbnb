from django.urls import path
from . import views
from .api_view import post_list_api, post_detail_api, post_search_api
from .views import PostList, PostDetail, PostByCategory, PostByTags

app_name = 'blog'

urlpatterns = [
    path("", PostList.as_view(), name="post_list"),
    path("<slug:slug>", PostDetail.as_view(), name="post_detail"),

    path("category/<str:slug>", PostByCategory.as_view(), name="post_by_category"),
    path("tags/<slug:slug>", PostByTags.as_view(), name="post_by_tags"),

    # api
    path("api/list", post_list_api, name="api_list_view"),
    path("api/list/<int:id>", post_detail_api, name="api_list_view"),
    path("api/list/filter/<str:query>", post_search_api, name="post_search_api"),
]
