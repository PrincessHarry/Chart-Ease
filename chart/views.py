from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.forms import SetPasswordForm, AuthenticationForm
from django.urls import reverse, reverse_lazy
from django.contrib.auth.forms import PasswordResetForm
from django.contrib.auth.views import PasswordResetView
from django.views.generic.edit import FormView
from django.contrib import messages
from django.template import loader
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.models import User
from django.contrib.auth.tokens import default_token_generator
from .models import *
from .forms import *




def home(request):
    return render(request, 'index.html')

def signin(request):
    form = CustomAuthenticationForm()
    
    if request.method == 'POST':
        username = request.POST["email"]
        password = request.POST["password"]
        
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('profile')
        else:
            messages.error(request, 'Username OR password does not exit')

    
    return render(request, 'signin.html',  {'form': form})
  
def signup(request):
    form = CustomUserCreationForm()

    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            
            messages.success(request, 'Account was created successfully')
            User.objects.create(related_user=user)
            return redirect('signin')
        else:
            messages.error(request, 'An error occurred during registration')

    return render(request, 'signup.html', {'form': form})



@login_required
def logoutUser(request):
     logout(request)
     return redirect('signin')


def reset_password(request):
    if request.method == 'POST':
        form = CustomPasswordResetForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            try:
                user = User.objects.get(email=email)
            except User.DoesNotExist:
                messages.error(request, 'Invalid email address.')
                return redirect('reset_password')

            # Generate a password reset token
            token = default_token_generator.make_token(user)

            # Store the token in the user's session
            request.session['reset_token'] = token
            request.session['reset_user_id'] = user.id

            # Redirect to the password reset confirmation page
            return redirect('reset_new_password')
    else:
        form = CustomPasswordResetForm()

    return render(request, 'reset_password.html', {'form': form})


def reset_new_password(request):
    token = request.session.get('reset_token')
    user_id = request.session.get('reset_user_id')

    if not token or not user_id:
        messages.error(request, 'Invalid password reset link.')
        return redirect('reset_password')

    try:
        user = User.objects.get(pk=user_id)
    except User.DoesNotExist:
        messages.error(request, 'Invalid password reset link.')
        return redirect('reset_password')

    if not default_token_generator.check_token(user, token):
        messages.error(request, 'Invalid password reset link.')
        return redirect('reset_password')
    
    if request.method == 'POST':
        form = CustomPasswordResetForm(request.POST)
        if form.is_valid():
            form.save(user)
            messages.success(request, 'Your password has been reset successfully.')
            return redirect('signin')
    else:
        form = CustomPasswordResetForm()

    return render(request, 'reset_new_password.html', {'form': form})




def profile(request):
   
   return render(request, 'profile.html')




def edit_profile(request):
    user = request.user  

    if request.method == 'POST':
        form = ProfileEditForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()
            
            return redirect('profile')  
    else:
        
        form = ProfileEditForm(instance=user)

    return render(request, 'edit-profile.html', {'form': form})
