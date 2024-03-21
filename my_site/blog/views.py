from django.shortcuts import render
from core.views import all_posts

print(all_posts)
def blog_posts(req):
    return render(req,'blog/all-posts.html', {'all_posts':all_posts})

def post_details(req, slug):
    for post in all_posts:
        if post['slug'] == slug:
            return render(req, 'blog/post-detail.html', {'post':post})