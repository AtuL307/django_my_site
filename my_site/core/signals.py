from django.dispatch import Signal, receiver
from django.core.mail import send_mail
from my_site.settings import EMAIL
# from django.contrib.auth.signals import user_logged_in
from django.template.loader import render_to_string


password_reset_mail = Signal()
user_logged_in_task = Signal()

@receiver(user_logged_in_task)
def send_login_email(sender, user_first_name, user_last_name, user_email, **kwargs):
    """
        Signal receiver function to send an email when a user logs in.
    """
 
    subject = 'Login Notification'
    message = f'Hello {user_first_name} {user_last_name},\n \b\b You have successfully logged in to our website.'
    from_email = EMAIL["EMAIL_HOST_USER"] 
    print(from_email)# Replace with your email
    to_email = [user_email]  # Assuming the user's email is stored in the email field
    print("login successful email send")
    # send_mail(subject, message, from_email, to_email)

    del subject, message, from_email, to_email


@receiver(password_reset_mail)
def send_password_reset_mail(sender, user_email, reset_link, **kwargs):
    
    """
        Mail send to user for password reset !
    """
    email_subject = 'Password Reset'
    email_body = render_to_string('core/txt/password_reset_email.txt', context={'reset_link': reset_link,})
    email = user_email
    print("password successful email send")
    #send_mail(email_subject, email_body, EMAIL, [email])     
    
    del email_subject, email_body, email