from django.dispatch import Signal, receiver
from django.core.mail import send_mail
from my_site.settings import EMAIL_HOST_USER
from django.contrib.auth.signals import user_logged_in
from django.template.loader import render_to_string


password_reset_mail = Signal()

@receiver(user_logged_in)
def send_login_email(sender, request, user, **kwargs):
    """
        Signal receiver function to send an email when a user logs in.
    """
    subject = 'Login Notification'
    message = f'Hello {user.first_name} {user.last_name},\n \b\b You have successfully logged in to our website.'
    from_email = EMAIL_HOST_USER  # Replace with your email
    to_email = [user.email]  # Assuming the user's email is stored in the email field
    print("login successful email send")
    # send_mail(subject, message, from_email, to_email)


@receiver(password_reset_mail)
def send_password_reset_mail(sender, request, user, reset_link, **kwargs):
    
    """
        Mail send to user for password reset !
    """
    email_subject = 'Password Reset'
    email_body = render_to_string('core/txt/password_reset_email.txt', context={'reset_link': reset_link,})
    email = user.email
    print("password successful email send")
    # send_mail(email_subject, email_body, EMAIL_HOST_USER, [email])     