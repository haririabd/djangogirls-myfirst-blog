from django.shortcuts import render
from django.utils import timezone
from .models import Post #We import Post model to be use im here
from django.shortcuts import render, get_object_or_404

# Create your views here.
def post_list(request):
    # We create a variable named posts for our QuerySet
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    # We pass our QuerySet above to the template by assigning the querypost to the template as posts
    return render(request, 'blog/post_list.html', {'posts' : posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})