from django.urls import path
from authentication import views as auth_views
from django.contrib.auth import views as django_auth_views


urlpatterns = [
    path('auth/register',auth_views.register, name="auth_register"),
    path('auth/login', auth_views.login, name="auth_login"),
    path('auth/password_reset/', auth_views.password_reset_request, name='password_reset_request'),
    path('password_reset/done/', django_auth_views.PasswordResetDoneView.as_view(template_name='registration/password_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', django_auth_views.PasswordResetConfirmView.as_view(template_name="registration/password_reset_confirm.html"), name='password_reset_confirm'),
    path('reset/done/', django_auth_views.PasswordResetCompleteView.as_view(template_name='registration/password_reset_complete.html'), name='password_reset_complete'),      
    
    # path('auth/change-password',auth_views.changePassword),
    # path('posts',auth_views.fetchPostsForRegularUser),
    # path('auth/freemium-register',auth_views.RegisterAndFetchPostsForFreemiumUser)
]