from django.shortcuts import render, get_object_or_404
from django.utils import timezone
#Include the model we have written in models.py
#The dot before models means current directory or current application. Both
# views.py and models.py are in the same directory. This means we can use . and
# the name of the file.
from .models import Post

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
