from django.urls import path
from . import views
from . import class_views


urlpatterns = [
    
  # Function view
    # path('posts/', views.blog_posts, name='all-posts-page'), 
    # path('posts/<slug:slug>/', views.post_details, name='postDetail-page'), 
  
  # Class view
    path('posts/',class_views.AllBlogPostsListView.as_view(), name='all-posts-page'),
    path('my-posts/',class_views.MyPostsListView.as_view(), name='my-posts'),
    path('posts/<slug:slug>/', class_views.PostDetailView.as_view(), name='postDetail-page'),
    path('read-later/',class_views.ReadLaterView.as_view(), name="read-later"),
    path('add-author/',class_views.AuthorView.as_view(), name= 'add-author'),
    path('add-post/',class_views.AddPostView.as_view(), name='add-post'),
    path('add-tag/',class_views.AddTagView.as_view(), name="add-tag")
    
]
 