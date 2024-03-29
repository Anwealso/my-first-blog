from django.shortcuts import render, get_object_or_404
from django.utils import timezone
#Include the model we have written in models.py
#The dot before models means current directory or current application. Both
# views.py and models.py are in the same directory. This means we can use . and
# the name of the file.
from .models import Post
from .forms import PostForm

# Create your views here.

def post_list(request):
    """post_list():
    A function that takes request and will return the value it gets from calling
    another function render that will render (put together) our template
    blog/post_list.html."""
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts' : posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post' : post})

def post_new(request):
    form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})

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
    return render(request, 'blog/post_edit.html', {'form': form})
