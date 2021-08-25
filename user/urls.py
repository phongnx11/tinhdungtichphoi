from django.contrib import admin
from django.urls import path
from .views import *
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', home, name="home"),
    path('register', register_attempt, name="register_attempt"),
    path('accounts/login/', login_attempt, name="login_attempt"),
    path('token', token_send, name="token_send"),
    path('success', success, name='success'),
    path('verify/<auth_token>', verify, name="verify"),
    path('error', error_page, name="error"),
    path('logout/',Dangxuat,name='dangxuat'),
    path('password_change/',auth_views.PasswordChangeView.as_view(), name='password_change'),
    path('password_change/done',auth_views.PasswordChangeDoneView.as_view(), name='password_change_done'),
    path('password_reset/',auth_views.PasswordResetView.as_view(),name='password_reset'),
    path('password_reset_done/',auth_views.PasswordResetDoneView.as_view(),name='password_reset_done'),
    path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(),name='password_reset_confirm'),
    path('reset/done/',auth_views.PasswordResetCompleteView.as_view(),name='password_reset_complete'),
    path("myfile/", myfile,name='myfile'),
    path("upload/", uploadfile, name="upload")
    # path("myfile/", FileFieldView.as_view(), name="upload")


]
