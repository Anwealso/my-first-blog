from django.urls import path
# Importing the collection of views from views.py in this directory
from . import views

# Assigning a view called post_list to the root URL
# 'post_list' isthe name of the URL that will be used to identify the view
urlpatterns = [
    # Arguments: str:url, obj:view, str:nameOfPage
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new/', views.post_new, name='post_new'),
]
