from django import forms
from django.core import validators
from django.contrib import messages
from django.contrib.auth.models import User
from . models import Comment, Post, Author, Tag
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import UserCreationForm, UserChangeForm


class TagForm(forms.ModelForm):
    
    class Meta:
        model = Tag
        fields = "__all__"
        labels ={
            "caption" : "Your Favorite Tag"
        }

class AuthorForm(forms.ModelForm):
    
    class Meta:
        model = Author
        fields = "__all__"
        labels = {
            "first_name" : "First Name",
            "last_name" : "Last Name",
            "email_address" : "Email",
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
                    "required" : "Name field is empty !"            
                },
            "user_email":{
                    "required" : "Email field is empty !" 
                },
            "text":{
                    "required" : "Text field is empty !" 
                },
        }
        
        
class SignUpForm(UserCreationForm):
    
    def clean_email(self):
        
        cleaned_data = super().clean()
        new_email = cleaned_data.get("email") 
        
        validate_email = User.objects.filter(email = new_email).exists()
        
        if new_email == "" and len(new_email) == 0:
              raise ValidationError ("This field is required.")
          
        elif validate_email == True:
            raise ValidationError (" This email address is already exist !!")
        
        else:
            return new_email
        
        
    def clean_first_name(self):
        cleaned_data = super().clean()   
        first_name = cleaned_data.get("first_name") 
        
        if first_name == "" and len(first_name) == 0:
            raise ValidationError ("This field is required.")
        else:    
            return first_name
        
    def clean_last_name(self):
        cleaned_data = super().clean()   
        l_name = cleaned_data.get("last_name") 
        
        if l_name == "" and len(l_name) == 0:
            raise ValidationError ("This field is required.")
        else:    
            return l_name
        
        
    class Meta:
        model = User
        fields = ("username", "first_name", "last_name", "email")
        labels = {"email": "Email"}

        
        
class EditUserProfileForm(UserChangeForm):
    password = None
    class Meta:
        model = User
        fields = ("username", "first_name", "last_name", "email")
        labels = {"email": "Email"}
        widgets = {
            "username" : forms.TextInput(attrs = {'readonly' : True}),
        }
    
            
    def clean_email(self):
        cleaned_data = super().clean()
        new_email = cleaned_data.get("email") 
        
        validate_email = User.objects.filter(email = new_email).exists()
                  
        if validate_email == True:
            raise ValidationError (" This email address is already exist !!")
        
        else:
            return new_email