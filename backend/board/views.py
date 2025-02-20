from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from django.http import JsonResponse
from django.template.loader import render_to_string
from rest_framework import viewsets
from .models import Post
from .serializers import PostSerializer

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

# /dashboard
@csrf_exempt # iframe 요청을 위해 CSRF 비활성화 (주의: 보안 검토 필요)
def dashboard(request):
    posts = Post.objects.all()
    return render(request, 'dashboard.html', {'posts': posts})

# /api/dashboard
@csrf_exempt
def api_dashboard(request):
    posts = Post.objects.all()
    serializer = PostSerializer(posts, many=True)
    return JsonResponse({'posts': serializer.data}, safe=False)