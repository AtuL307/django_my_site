from . models import Post
from django.views.decorators.http import require_http_methods
from django.shortcuts import render

# Create your views here
@require_http_methods(["GET"])
def index(req):
    try:
        latest_posts = Post.objects.all().order_by("-date")[:3]
        return render (req, 'core/index.html', {'posts': latest_posts})
        
    except Exception as err:
        pass