from django.shortcuts import render, get_object_or_404
from django.views.decorators.http import require_http_methods
from django.http import HttpResponse
from core.models import Post

@require_http_methods(["GET"])
def blog_posts(req):
    try:
        all_posts = Post.objects.all()
        return render(req,'blog/all-posts.html', {'all_posts':all_posts})
        
    except Exception as err:
        pass
    
@require_http_methods(["GET"])
def post_details(req, slug):
    try:
        post = get_object_or_404(Post, slug = slug)
        post_tag = post.tag.all() 
        return render(req, 'blog/post-detail.html', {'post':post, "post_tag": post_tag })
    except Exception as err:
            return HttpResponse(err)
   