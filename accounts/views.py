from django.shortcuts import render, redirect, reverse, HttpResponse
from django.contrib import auth, messages
from .forms import UserLoginForm

# Create your views here.
def index(request):
    return render(request, "accounts/index.template.html")
    
"""
This is the logout function
"""
def logout(request):
    auth.logout(request)
    messages.success(request, "You have been logged out")
    return redirect(index)

"""
This is login function
"""
def login(request):
    form = UserLoginForm()
    return render(request, 'accounts/login.template.html', {
        'form':form
    })