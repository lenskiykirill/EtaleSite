from django.shortcuts import render, get_object_or_404
from django.utils import timezone, safestring

# Create your views here.
from .models import Post

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts':posts,})

def view_post(request, handle):
    post = get_object_or_404(Post, handle=handle)
    post.text = safestring.mark_safe(post.text)
    print(post)
    return render(request, 'blog/view_post.html', {'post':post})
