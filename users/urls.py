from django.urls import path
from . import views
from django.contrib.auth.views import (LoginView,PasswordChangeView,PasswordChangeDoneView,
                                                 PasswordResetView,PasswordResetConfirmView,
                                                 PasswordResetCompleteView,PasswordResetDoneView)
urlpatterns = [
    path('register/',views.Register.as_view(),name ='register'),
    path('login/', LoginView.as_view(template_name='users/login.html') ,name = 'login'),
    path('password_change/', PasswordChangeView.
         as_view(template_name = 'users/password_change.html'), name='password_change'),
    
    path('password_change/done/',PasswordChangeDoneView
         .as_view(template_name = 'users/password_change_done.html'), name='password_change_done'),
    
    path('password_reset/', PasswordResetView
         .as_view(template_name = 'users/password_reset_email.html'), name='password_reset'),
    
    path('password_reset/done/', PasswordResetDoneView
         .as_view(template_name = 'users/password_reset_done.html'), name='password_reset_done'),
    
    path('reset/<uidb64>/<token>/', PasswordResetConfirmView
         .as_view(template_name = 'users/password_reset_confirm.html'), name='password_reset_confirm'),
    
    path('reset/done/', PasswordResetCompleteView
         .as_view(template_name = 'users/password_reset_complete.html'), name='password_reset_complete'),

]   