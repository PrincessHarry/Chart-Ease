from django import forms
from .models import *
from django.contrib.auth.forms import PasswordResetForm
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from django.contrib.auth import get_user_model

# User = get_user_model()

class CustomUserCreationForm(UserCreationForm):
     class Meta:
        model = get_user_model()
        fields = ('username', 'email', 'image',  'phone_number', 'dob', 'organization_company', 'job_title',  'password1', 'password2', 'terms_accepted')
        widgets = {
            'username': forms.TextInput(attrs={'placeholder': 'Name'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Email Address'}),
            'phone_number': forms.TextInput(attrs={'placeholder': 'Phone Number'}),
            'dob': forms.TextInput(attrs={'placeholder': '27/06/2002'}),
            'organization_company': forms.TextInput(attrs={'placeholder': 'Organization/company'}),
            'job_title': forms.TextInput(attrs={'placeholder': 'Job_title'}),
            'password1': forms.PasswordInput(attrs={'placeholder': '',  'autocomplete': 'off'}),
            'password2': forms.PasswordInput(attrs={'placeholder': '',  'autocomplete': 'off'}),
        }
            
        
            
        
class CustomAuthenticationForm(AuthenticationForm):
    email = forms.EmailField(widget=forms.TextInput(attrs={'autofocus': True}))
    remember_me = forms.BooleanField( required=False, widget=forms.CheckboxInput(attrs={'class': 'form-check-input'}),
    )




class ProfileEditForm(forms.ModelForm):
     class Meta:
          model = User
          fields = ['image', 'username',  'email', 'phone_number', 'job_title', 'organization_company', 'dob']
          widgets = {'image': forms.ClearableFileInput(attrs={'multiple': False})}
class CustomPasswordResetForm(PasswordResetForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email Address'}))
   
      
    new_password1 = forms.CharField(
        label='New Password',
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Enter new password'}),
    )
    new_password2 = forms.CharField(
        label='Confirm New Password',
        widget=forms.PasswordInput(attrs={'class': 'form-control',  'placeholder': 'Confirm new password'}),
    )
