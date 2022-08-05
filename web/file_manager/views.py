from django.shortcuts import render, redirect
from django.auth.contrib import authenticate, login
from django.http import HttpResponseForbidden
from .models import *
from .forms import *

def auth_login(request):
    if request.method == 'POST':
        form = LoginForm(request.data)
        if form.is_valid():
            username = request.cleaned_data['username']
            password = request.cleaned_data['password']
            remember_me = request.cleaned_data['remember_me']
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                if not remember_me:
                    request.session.set_expiry(0)
                    request.session.modified = True
                return redirect('/home')
        return HttpResponseForbidden()
    else:
        form = LoginForm()
        return render(request, 'file_manager/login.html', {'form': form})

def get_home(request):
    if request.user.is_authenticated:
        return render(request, 'file_manager/home.html')
    return redirect('/login')