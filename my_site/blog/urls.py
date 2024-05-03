from django.urls import path
from . import views
from . import class_views


urlpatterns = [
    
  # Function view
    # path('posts/', views.blog_posts, name='all-posts-page'), 
    # path('posts/<slug:slug>/', views.post_details, name='postDetail-page'), 
  
  # Class view
    path('posts/',class_views.AllBlogPostsListView.as_view(), name='all-posts-page'),
    path('posts/<slug:slug>/', class_views.PostDetailView.as_view(), name='postDetail-page'),
    
]
 