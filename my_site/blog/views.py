from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def blog(req):
    return HttpResponse('<h1>Blog</h1>')