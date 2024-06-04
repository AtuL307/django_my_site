from django.urls import path, include
from . import views
from . import class_views
urlpatterns = [
    # path('',views.index, name='index'),
    
    path('',class_views.IndexPageListView.as_view(), name= 'index'),
    path('MyAccount/',class_views.MyAccountView.as_view(), name="profile"),
    path('signup/',class_views.SignUpView.as_view(), name="sign-up"),
    path('login/',class_views.LogInView.as_view(), name="sign-in"),
    path('MyAccount/logout/',class_views.LogOutView.as_view(), name="log-out"),
    path('MyAccount/change-password/',class_views.ChangePasswordView.as_view(), name="change-password"),
   
    path('password-reset/',class_views.PasswordResetView.as_view(), name="password-reset"),
    path('password-reset-confirm/<uid64>/<token>',class_views.PasswordResetConfirmView.as_view(), name="password-reset-confirm"),
    
    path('blog/', include('blog.urls')),
    
]
