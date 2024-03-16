from django.urls import path
from . import views
urlpatterns = [
    path('posts', views.blog, name='posts'),
    #path('posts/<slug>'),
    
]
