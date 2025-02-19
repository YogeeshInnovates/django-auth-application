from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from .views import signup_view, forgot_password_view, login_view
urlpatterns = [
    path('', views.login_view, name='login'),
    path('signup/', views.signup_view, name='signup'),
path('forgot-password/', views.forgot_password_view, name='forgot_password'),
path('change-password/', views.change_password_view, name='change_password'),
path('dashboard/', views.dashboard_view, name='dashboard'),
path('profile/', views.profile_view, name='profile'),
path('logout/', views.logout_view, name='logout'),
 
    path('forgot-password/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),



]
