from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
# Create your views here.

def index(req):
    indexTemplate = loader.get_template('core/index.html')
    return HttpResponse (indexTemplate.render())