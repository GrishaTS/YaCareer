from django.contrib.auth.views import (LoginView, LogoutView,
                                       PasswordChangeDoneView,
                                       PasswordChangeView,
                                       PasswordResetCompleteView,
                                       PasswordResetConfirmView,
                                       PasswordResetDoneView,
                                       PasswordResetView)
from django.urls import path

app_name = 'auth'

urlpatterns = (
    path(
        'login/',
        LoginView.as_view(
            template_name='users/registration/login.html',
            redirect_authenticated_user=True,
        ),
        name='login',
    ),
    path(
        'logout/',
        LogoutView.as_view(
            template_name='users/registration/logout.html',
        ),
        name='logout',
    ),
    path(
        'password_change/',
        PasswordChangeView.as_view(
            template_name='users/registration/password_change.html',
        ),
        name='password_change',
    ),
    path(
        'password_change/done/',
        PasswordChangeDoneView.as_view(
            template_name='users/registration/password_change_done.html',
        ),
        name='password_change_done',
    ),
    path(
        'password_reset/',
        PasswordResetView.as_view(
            template_name='users/registration/password_reset.html',
        ),
        name='password_reset',
    ),
    path(
        'reset/done/',
        PasswordResetCompleteView.as_view(
            template_name='users/registration/password_reset_complete.html',
        ),
        name='password_reset_complete',
    ),
    path(
        'reset/<uidb64>/<token>/',
        PasswordResetConfirmView.as_view(
            template_name='users/registration/password_reset_confirm.html',
        ),
        name='password_reset_confirm',
    ),
    path(
        'password_reset/done/',
        PasswordResetDoneView.as_view(
            template_name='users/registration/password_reset_done.html',
        ),
        name='password_reset_done',
    ),
)
