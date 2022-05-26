from rest_framework.decorators import api_view

from .models import Post
from .serializer import PostSerializer

from rest_framework.response import Response

@api_view(['GET'])
def postlistapi(request):
      all_post = Post.objects.all()
      data = PostSerializer(all_post,many=True).data
      return Response({'data': data})
