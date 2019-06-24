from django.urls import path
# Importing the collection of views from views.py in this directory
from . import views

urlpatterns = [
    # Assigning a view called post_list to the root URL
    # 'post_list' isthe name of the URL that will be used to identify the view
    path('', views.post_list, name='post_list'),
]
