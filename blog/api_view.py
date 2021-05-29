from django.db.models import Q
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response

from blog.models import Post
from blog.serializers import PostSerializer


@api_view(['GET'])
def post_list_api(request):
    all_posts = Post.objects.all()
    data = PostSerializer(all_posts, many=True).data
    return Response({'data': data})


@api_view(['GET'])
def post_detail_api(request, id):
    post = get_object_or_404(Post, id=id)
    data = PostSerializer(post).data
    return Response({'data': data})


@api_view(['GET'])
def post_search_api(request, query):
    posts = Post.objects.filter(
        Q(title__icontains=query) |
        Q(description__icontains=query)
    )
    data = PostSerializer(posts, many=True).data
    return Response({'data': data})