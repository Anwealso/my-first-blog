from django.shortcuts import render

# Create your views here.

def post_list(request):
    """post_list():
    A function that takes request and will return the value it gets from calling
    another function render that will render (put together) our template
    blog/post_list.html."""
    return render(request, 'blog/post_list.html', {})
