from typing import Any
from django.db.models.base import Model as Model
from django.db.models.query import QuerySet
from core.models import Post
from django.views.generic import ListView, DetailView

class AllBlogPostsListView(ListView):
    model = Post
    queryset = Post.objects.all().order_by("-date")[:3]
    context_object_name = 'all_posts'
    template_name='blog/all-posts.html'


class PostDetailView(DetailView):
    model = Post
    query_pk_and_slug = True
    slug_url_kwarg = 'slug'
    context_object_name = 'post'
    template_name='blog/post-detail.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        print(kwargs['object'])
        print(self.object)
        context['post_tag'] = self.object.tag.all()
        return context