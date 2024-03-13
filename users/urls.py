from django.urls import path
from . import views
from .views import user_profile, user_login, user_logout
from .views import my_receptions

from django.contrib.auth import views as auth_views
from .views import csrf_token_endpoint, RecoverAccount, SendTempPassword, CustomPasswordResetView, CustomPasswordResetDone, CustomPasswordResetConfirmView

app_name = 'users'
urlpatterns = [

 path("signup/", views.register, name="signup"),
 path('profile/', user_profile, name='user_profile'),
 path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('api/recover', RecoverAccount.as_view(), name='recover-account'),
    path('api/send-temp-password', SendTempPassword.as_view(), name='send-temp-password'),
    path('password_reset/', CustomPasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', views.CustomPasswordResetDone.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', CustomPasswordResetConfirmView.as_view(), name='password_reset_confirm'),

    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
 path('csrf_token_endpoint/', csrf_token_endpoint, name='csrf_token_endpoint'),


]