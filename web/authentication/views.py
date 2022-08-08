from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseForbidden
from authentication.forms import *

BUTTON_LOGIN = 'login'
BUTTON_REGISTER = 'register'


def home(request):
    if request.method == 'POST':
        if BUTTON_LOGIN in request.POST:
            return auth_login(request)
        elif BUTTON_REGISTER in request.POST:
            return register(request)
    login_form = LoginForm()
    register_form = RegisterForm()
    return render(request, 'authentication/index.html',
                  {'login_form': login_form, 'register_form': register_form, 'type': 'login'})

def auth_login(request):
    form = LoginForm(request.POST)
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
            return redirect('home')
    return HttpResponseForbidden()


def register(request):
    form = RegisterForm(request.POST)
    login_form = LoginForm()
    register_form = RegisterForm()
    if form.is_valid():
        form.save()
        return render(request, 'authentication/index.html',
                      {'login_form': login_form, 'register_form': register_form, 'type': 'login'})
    return render(request, 'authentication/index.html',
                  {'login_form': login_form, 'register_form': form, 'type': 'register'})

def auth_logout(request):
    logout(request)
    login_form = LoginForm()
    register_form = RegisterForm()
    return render(request, 'authentication/index.html',
                  {'login_form': login_form, 'register_form': register_form, 'type': 'login'})
