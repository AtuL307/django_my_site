import blog.signals

from core.models import Post, Author
from django.db import IntegrityError
from core.forms import CommentForm, PostForm,AuthorForm, TagForm
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.utils.text import slugify
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

        return HttpResponseRedirect(reverse("all-posts-page"))  
    
    
class AddPostView(View):
    def get(self, request):
        post_form = PostForm()
        return render(request, 'blog/add_post.html', context={"post_form": post_form})

    def post(self, request):
        post_form = PostForm(request.POST, request.FILES)
        
        if post_form.is_valid():
            
            post = post_form.save(commit=False)  
            post.slug = slugify(post.title)                 
          
            try:
                post.save()
                
            except IntegrityError as err:
                print("Data could not be saved due to IntegrityError:", err)
                return render(request, 'blog/add_post.html', context={"post_form": post_form, "error": str(err), "post_title": post.title})            

                    
            return HttpResponseRedirect(reverse("all-posts-page"))

        else:
            post_form = PostForm()
            return render(request, 'blog/add_post.html', context={"post_form": post_form})


class AuthorView(View):
    def get(self, request):
        author_form = AuthorForm()
        return render(request, 'blog/add_author.html', context={"author_form": author_form})

    def post(self, request, *args, **kwargs):
        author_form = AuthorForm(request.POST)
        
        if author_form.is_valid():
            
            try:                
                
                author_form.save() # This will trigger the "post_save" signal to function "author_send_verification_mail"
                
            except IntegrityError as err:
                print("Data could not be saved due to IntegrityError:", err)
     
        else:
            author_form = AuthorForm()
            return render(request, 'blog/add_author.html', context={"author_form": author_form})
        
     
        return HttpResponseRedirect(reverse("add-post"))
    
    
class AddTagView(View):
    
    def get(self, request):
        tag_form = TagForm()
        return render(request, 'blog/tag.html', context={"tag_form": tag_form} )

    def post(self, request):
        tag_form = TagForm(request.POST)
        
        if tag_form.is_valid():
            tag_form.save()
            return HttpResponseRedirect(reverse("add-post"))
        else:
            
            tag_form = TagForm()
            return render(request, 'blog/tag.html', context={"tag_form": tag_form} )