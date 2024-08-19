from django.shortcuts import render
from django.utils import timezone
from .models import Post #We import Post model to be use im here
from django.shortcuts import render, get_object_or_404
from .forms import PostForm
from django.shortcuts import redirect

# Create your views here.
def post_list(request):
    # We create a variable named posts for our QuerySet
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    # We pass our QuerySet above to the template by assigning the querypost to the template as posts
    return render(request, 'blog/post_list.html', {'posts' : posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form':form})
# without if / else, we are just displaying the forms. Nothing happens when click save

def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})