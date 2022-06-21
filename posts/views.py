from django.shortcuts import render
# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response

from posts.models import Post, videosYoutube
from django.core.paginator import Paginator

from posts.serializer import PostSerializer


def index(request):
    queryset = Post.objects.all()
    context = {
        'post': queryset
    }
    return render(request, 'index.html', context)


def pagepost(request, slug):
    post = Post.objects.get(slug=slug)
    context = {'post': post}
    return render(request, "pagepost.html", context)


def posts(request):
    queryset = Post.objects.all()
    context = {
        'object_list': queryset
    }
    return render(request, 'post.html', context)


def contact(request):
    return render(request, 'contact.html', {})


def about(request):
    return render(request, 'about.html', {})


def videos(request):
    videos = videosYoutube.objects.all()
    context = {
        'videos': videos
    }
    return render(request, 'videos.html', context)


@api_view(['GET'])
def postlistapi(request):
    all_posts = Post.objects.all()
    data = PostSerializer(all_posts, many=True).data
    return Response({'data': data})
