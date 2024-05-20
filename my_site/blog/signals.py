import boto3
import json

from django.db.models.signals import post_save
from django.dispatch import Signal, receiver
from django.core.mail import send_mail

from my_site.settings import EMAIL_HOST_USER
from core.models import Author, Post

    
@receiver(post_save, sender=Author)
def author_send_verification_mail(sender, instance, **kwargs):

    client = boto3.client('ses')
    
    client.verify_email_identity(
        EmailAddress = instance.email_address
    )

@receiver(post_save, sender=Post)
def post_upload_email(sender, instance, **kwargs):
    
    f_name, l_name = str(instance.author).split(" ")
    author_email = Author.objects.get(first_name = f_name, last_name = l_name).email_address       
    
    subject = "Thank you for posting your Blog !"
    message = f"Dear {instance.author}, \n \b\b\b\b\bThanks for posting your blog \"{instance.title}\" on our website !"
    to_email = [author_email]
    
    send_mail(subject, message, from_email=EMAIL_HOST_USER, recipient_list=to_email, fail_silently= False)
    
    
    
    
    
""" AWS Lambda Trigger"""   
    # payload = {"author_email" : instance.email_address }
    # author_email = json.dumps(payload)
    # client = boto3.client('lambda')
    # client.invoke(
    #     FunctionName = 'arn:aws:lambda:ap-south-1:211125332700:function:my-function',
    #     Payload=f'{author_email}',
    # )
    # print(author_email)