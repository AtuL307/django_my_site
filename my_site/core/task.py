from .signals import password_reset_mail, user_logged_in_task
# from my_site.settings import EMAIL_HOST_USER
# from django.core.mail import send_mail
from celery import shared_task

import time

@shared_task
def send_email_password_reset_confirmation(email, reset_link):
    password_reset_mail.send(sender="password_rest_email" , user_email=email, reset_link = reset_link)
    return "Done"

@shared_task
def send_login_email_to_user(user_first_name, user_last_name, user_email):
    user_logged_in_task.send(sender="login_success_email", user_first_name=user_first_name,
                            user_last_name=user_last_name, 
                            user_email=user_email)
    
    return "Done"
    