from django.urls import path
from django.contrib.auth import views
from account.views import login, dashboard
from .views import SignUpView, activate
urlpatterns = [
    path('login/', login, name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('logout-then-login/', views.logout_then_login, name='logout_then_login'),
    path('password-reset/', views.PasswordResetView.as_view(), name='password_reset'),
    path('password-reset/done/', views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('password-reset/confirm/str: <uidb64>/str: <token>/', views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('password-reset/complete/', views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    path('signup/', SignUpView, name='signup'),
    path('activate/str: <uidb64>/str: <token>/',
        activate, name='activate'),
    path('', dashboard, name='dashboard'),
]