from django.shortcuts import render

# Create your views here.

def blog_posts(req):
    return render(req,'blog/all-posts.html')

def post_details(req):
   pass