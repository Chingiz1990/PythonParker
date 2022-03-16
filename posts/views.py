from django.shortcuts import render

# Create your views here.

# zdes' nastraivaetsya otobrajenie dannyh

from posts.models import Post

def post_list(request):
    posts = Post.objects.all()
    return render(request, 'blog/blog.html', context={'post': posts})
