from django import forms
from . models import Comment, Post, Tag

class TagForm(forms.ModelForm):
    
    class Meta:
        model = Tag
        fields = "__all__"
        labels ={
            "caption" : "Your Favorite Tag"
        }

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ["date", "slug"]
        labels ={
            "title" : "Blog Title",
            "excerpt" : "Blog Excerpt",
            "images" : "Blog Image",
            "content" : "Blog Content",
            "author" : "Blog Author",
            "tag" : "Blog Tags"
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        # fields = ['user_name', 'user_email', 'text']
        exclude = ['post']
        labels = {
            "user_name" : "Your Name",
            "user_email": "Your Email",
            "text": "Your Comment",
        }
        error_messages = {
            "user_name" : {
                    "required" : "Your name is empty!"            
                },
            "user_email":{
                    "required" : "Your email is empty!" 
                },
            "text":{
                    "required" : "Your text is empty!" 
                },
        }