from django.contrib.auth import authenticate, login,update_session_auth_hash,logout
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm,PasswordResetForm,PasswordChangeForm
from .forms import CustomUserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.mail import send_mail

def login_view(request):
   
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
            
                return redirect('dashboard')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})



def signup_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # Redirect to login page after successful sign-up
    else:
        form = CustomUserCreationForm()
    
    return render(request, 'signup.html', {'form': form})


def forgot_password_view(request):
    if request.method == 'POST':
        form = PasswordResetForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            associated_users = User.objects.filter(email=email)  # Ensure email exists in database
            
            if associated_users.exists():
                form.save(request=request)  # Sends email with reset link
                return redirect('password_reset_done')  # Redirect to confirmation page
            else:
                form.add_error('email', 'No user found with this email')  # Show error if email doesn't exist
    else:
        form = PasswordResetForm()
    
    return render(request, 'forgot_password.html', {'form': form})


def change_password_view(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Keeps user logged in after password change
            logout(request)  # Force logout after password change
            return redirect('login')  # Redirect to login page
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'change_password.html', {'form': form})

@login_required
def dashboard_view(request):
    return render(request, 'dashboard.html')


@login_required
def profile_view(request):
    return render(request, 'profile.html')


def logout_view(request):
    logout(request)
    return redirect('login')