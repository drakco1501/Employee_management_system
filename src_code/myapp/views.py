from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.hashers import check_password
from django.http import HttpRequest, HttpResponse
from .models import *
# Create your views here.

def home(request):
    return render(request, 'myapp/home.html')

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        try:
            user = cust_login.objects.get(user=username)
            
            # Check if password matches
            if check_password(password, user.password):
                request.session['user_id'] = user.id
                request.session['user'] = user.user
                request.session['is_user_logged_in'] = True
                
                messages.success(request, f'Welcome, {user.user}')
                return redirect('home')
            else:
                messages.error(request, 'Invalid username or password.')
        
        except user.DoesNotExist:
            messages.error(request, 'Invalid username or password.')
    
    return render(request, 'myapp/login.html')



def logout(request):
    if 'user_id' in request.session:
        del request.session['user_id']
    if 'user' in request.session:
        del request.session['user']
    if 'is_user_logged_in' in request.session:
        del request.session['is_user_logged_in']
    
    messages.success(request, 'You have been logged out successfully.')
    return redirect('login')