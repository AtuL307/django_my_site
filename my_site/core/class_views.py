import datetime
import secrets

from .models import Post
from django.views import View
from django.urls import reverse
from django.contrib import messages
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.views.generic.list import ListView
from core.forms import SignUpForm, EditUserProfileForm
from django.utils.encoding import force_bytes, force_str
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.utils.dateparse import parse_datetime

from .signals import password_reset_mail

##########################  HOME PAGE  ##########################
   
class IndexPageListView(ListView):
    
    model = Post
    # queryset = Post.objects.all().order_by("-date")[:3]
    context_object_name = 'posts'
    ordering = ['-date']
    template_name= 'core/index.html'
    
    
    def get_queryset(self):
        query =  super().get_queryset()   
        data = query[:3]
        # print(data)
        return data
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        if self.request.user.is_authenticated:
            context['user'] = self.request.user
             
        return context
    
    
##########################  SIGNUP  ##########################

class SignUpView(View):
    """
        dispatch() allows you to customize the request handling before it reaches 
        the actual view method (like get() or post()).
    """   
    def dispatch(self, request, *args, **kwargs):
        
        if not self.request.user.is_authenticated:
            return super().dispatch(request, *args, **kwargs)
        else:
            return HttpResponseRedirect(reverse("sign-up"))
        
    def get(self, request):
        
        sign_up_form = SignUpForm()
        return render(request, "core/signup.html", context= {"sign_up_form" : sign_up_form })

            
    def post(self, request):
        
        sign_up = SignUpForm(request.POST)
        
        if sign_up.is_valid():
            sign_up.save()
            messages.success(request, "Your Account Successfully Created !!")
            return HttpResponseRedirect(reverse('sign-in')) 
            
        return render(request, "core/signup.html", context = { "sign_up_form" : sign_up })



##########################  USER PROFILE  ##########################

class MyAccountView(View):
    """
        dispatch() allows you to customize the request handling before it reaches 
        the actual view method (like get() or post()) .
    """
    def dispatch(self, request, *args, **kwargs):
        
        if self.request.user.is_authenticated:
            return super().dispatch(request, *args, **kwargs)
        else:
            return HttpResponseRedirect(reverse('sign-in'))
    
    def get(self, request):
           
        profile_form = EditUserProfileForm(instance = request.user)
        return render(request, "core/profile.html", context={"profile_form":profile_form})
    
    def post(self, request):
         
        profile_form = EditUserProfileForm(request.POST, instance = request.user )
            
        if profile_form.is_valid():
                
            profile_form.save()
                
            messages.success(request, "Successfully update profile !!")    
            return HttpResponseRedirect(reverse('profile'))
            
        return render(request, "core/profile.html", context={"profile_form":profile_form})
        
            
##########################  LOGIN  ##########################

class LogInView(View):
    """
        dispatch() allows you to customize the request handling before it reaches 
        the actual view method (like get() or post()) .
    """   
    def dispatch(self, request, *args, **kwargs):
        
        if not self.request.user.is_authenticated:
            return super().dispatch(request, *args, **kwargs)
        else:
            return HttpResponseRedirect(reverse('sign-in')) 
        
        
    def get(self, request):        

        log_in_form = AuthenticationForm()
        return render(request, "core/login.html", context={"sign_in_form":log_in_form})

        
    def post(self, request):
        
        log_in_form = AuthenticationForm(request, data = request.POST)

        if log_in_form.is_valid():                   
            username = log_in_form.cleaned_data['username']
            password = log_in_form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            
                        
            if user is not None:
                login(request, user)
                messages.success(request, "Login in successfully !")
                return HttpResponseRedirect(reverse('index'))
            else:
                messages.error(request, "Failed to log in")
                
                
        return render(request, "core/login.html", context={"sign_in_form":log_in_form})
        
        
##########################  LOGOUT  ##########################

class LogOutView(View):
    """
        dispatch() allows you to customize the request handling before it reaches 
        the actual view method (like get() or post()) .
    """    
    
    def dispatch(self, request, *args, **kwargs):
        
        if self.request.user.is_authenticated:
            return super().dispatch(request, *args, **kwargs)
        else:
            return HttpResponseRedirect(reverse('index'))
    
    def get(self, request):
        
        logout(request)
        messages.success(request, "Successfully Logout !")
        return HttpResponseRedirect(reverse("index"))



##########################  Change Password  ##########################

class ChangePasswordView(View):
    """
        dispatch() allows you to customize the request handling before it reaches 
        the actual view method (like get() or post()) .
    """
    def dispatch(self, request, *args, **kwargs):
        
        if self.request.user.is_authenticated:
            return super().dispatch(request, *args, **kwargs)
        else:
            messages.error(request, "Login required for change password !!")
            return HttpResponseRedirect(reverse('sign-in')) 
        
    def get(self, request):       
        
        change_pass = PasswordChangeForm(request.user)
        return render(request, 'core/change_password.html', context={"change_pass": change_pass})

            
    def post(self, request):
        
        change_pass = PasswordChangeForm(request.user, request.POST)

        if change_pass.is_valid():
            
            change_pass.save()
            update_session_auth_hash(request, change_pass.user)
            messages.success(request, "Password change successfully !!")
            return HttpResponseRedirect(reverse('sign-in'))
        
        else:
            messages.error(request, "Failed to Change Password")
            
        return HttpResponseRedirect(reverse('change-password'))



##########################  Reset Password  ##########################

class PasswordResetView(View):
    
    def get(self, request):

        # request.session.flush()
        return render(request, 'core/password-rest.html')
        
    def post(self, request):

        email = request.POST['email']
        
        try :
            
            user = User.objects.get(email = email)

        except User.DoesNotExist:
            messages.error(request, 'User with this email address does not exist.')
        
        if user and user.is_active == True:
    
            token = default_token_generator.make_token(user)
            uid = urlsafe_base64_encode(force_bytes(user.pk))
            
            expiry_time = (datetime.datetime.now() + datetime.timedelta(minutes = 2)).isoformat()
            
            ### Store email expiry to session. ###
            request.session['password_expiry'] = expiry_time
            
            reset_link = request.build_absolute_uri(reverse("password-reset-confirm", kwargs={'uid64':uid, 'token':token}))
            
            ### send link using signals ###
            password_reset_mail.send(sender = self.__class__, request=request, user=user, reset_link = reset_link) 
            
            messages.success(request, "Password reset link has been sent to your email address")
            return HttpResponseRedirect(reverse('password-reset'))


########################## Password Rest Confirm  ##########################
   
class PasswordResetConfirmView(View):
    
    def get(self, request, uid64, token):
          
        try:
            uid = urlsafe_base64_decode(force_str(uid64))
            user = User.objects.get(pk=uid)
   
        except (TypeError, ValueError, OverflowError, User.DoesNotExist):
           user = None
    
        if user and default_token_generator.check_token(user, token):
            
            expiry_time_str = request.session.get('password_expiry')
            
            if expiry_time_str:

                expiry_time = parse_datetime(expiry_time_str)
                if datetime.datetime.now() < expiry_time:           
            
                    return render(request, "core/password_reset_confirm_form.html")
            
                else:
                    messages.error(request, "Your password rest session is over, try again to rest password.")
                    return HttpResponseRedirect(reverse("sign-in"))
            else:
                messages.error(request, "User data not match.")
                return HttpResponseRedirect(reverse("sign-in"))

        else:
            messages.error(request, "Invalid reset link.")
            return redirect("password-reset")
        
    def post(self, request, uid64, token):
        
        try:    
            uid = force_str(urlsafe_base64_decode(uid64))
            print(uid)
            user = User.objects.get(pk=uid)
            
        except (TypeError, ValueError, OverflowError, User.DoesNotExist):
           user = None
       
        if user and default_token_generator.check_token(user, token):
            new_password = request.POST.get('new_password')
            print(new_password)
            user.set_password(new_password)
            user.save()
                       
            ### Clear email_expiry session ###
            if 'password_expiry' in request.session:
                del request.session['password_expiry']
        
            messages.success(request, "Password successfully reset.")    
            return HttpResponseRedirect(reverse('sign-in'))
        
        else:
            messages.error(request, "There was an error resetting your password.")    
            return HttpResponseRedirect(reverse('password-reset'))