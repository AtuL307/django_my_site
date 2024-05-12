from core.models import Post
from core.forms import CommentForm
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.db.models.base import Model as Model
from django.views.generic import ListView
from django.views import View
from .helper_func import data_fetch, session_stored_post


class AllBlogPostsListView(ListView):
    model = Post
    queryset = Post.objects.all().order_by("-date")
    context_object_name = 'all_posts'
    template_name='blog/all-posts.html'

class PostDetailView(View):

    
    def get(self, request, slug):
        post = get_object_or_404(Post, slug = slug)
        comment_form = CommentForm()   
            
    #helper function
        is_saved_for_later = session_stored_post(post, request)
        context = data_fetch(post, comment_form, is_saved_for_later)
    
        return render(request, 'blog/post-detail.html', context)

    def post(self, request,slug):
        post = get_object_or_404(Post, slug = slug)
        comment_form = CommentForm(request.POST)
        
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.save()
            return HttpResponseRedirect(reverse('postDetail-page', args=[slug]))
        
        else:
        #helper function       
            is_saved_for_later = session_stored_post(post, request)
            context = data_fetch(post, comment_form,is_saved_for_later)
            return render('blog/post-detail.html', context)
    
class ReadLaterView(View):
    
    def get(self, request):
        stored_post = request.session.get("stored_post")
        context = {}
        if stored_post is None or len(stored_post) == 0:
            context["posts"] =[]
            context["has_posts"] = False
        else:
            posts = Post.objects.filter(id__in=stored_post)    
            context["posts"] = posts
            context["has_posts"] = True
            
        return render(request, 'blog/stored-posts.html', context)
                 
    def post(self, request):
        stored_post = request.session.get("stored_post")
        
        
        if stored_post is None:
            stored_post = []
            
        post_id = int(request.POST["post_id"])
        
        if post_id not in stored_post:
            stored_post.append(post_id)
        else:
            stored_post.remove(post_id)    
        
        request.session["stored_post"] = stored_post

        return HttpResponseRedirect("/")  
    