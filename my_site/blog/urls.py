from django.urls import path
from . import views
urlpatterns = [
    path('posts/', views.blog_posts, name='posts-page'),
    path('posts/<slug:slug>/', views.post_details, name='postDetail-page'),
    
]
