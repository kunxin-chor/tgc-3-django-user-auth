from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError

# our own user model
from .models import MyUser

class UserLoginForm(forms.Form):
    """Form is for user login"""
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
    
"""
User registration form
"""
class UserRegistrationForm(UserCreationForm):
    password1 = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(label="Password Confirmation", widget=forms.PasswordInput)
    
    class Meta:
        model = MyUser
        fields = ['email', 'username', 'password1', 'password2']