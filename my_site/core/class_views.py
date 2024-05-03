from typing import Any
from django.db.models.query import QuerySet
from .models import Post
from django.views.generic.list import ListView
    
class IndexPageListView(ListView):
    model = Post
    # queryset = Post.objects.all().order_by("-date")[:3]
    context_object_name = 'posts'
    ordering = ['-date']
    template_name= 'core/index.html'
    
    
    def get_queryset(self):
        query =  super().get_queryset()   
        data = query[:3]
        print(data)
        return data