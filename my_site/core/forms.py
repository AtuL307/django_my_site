from django import forms
from . models import Comment

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