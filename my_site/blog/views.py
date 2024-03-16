from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def blog_posts(req):
    return HttpResponse('<h1>Blog</h1>')

def post_details(req):
   pass