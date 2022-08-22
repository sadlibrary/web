from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseForbidden, JsonResponse, HttpResponse
from authentication.forms import *
from django.contrib.auth.decorators import login_required

BUTTON_LOGIN = 'login'
BUTTON_REGISTER = 'register'


def start_page(request):
    return render(request, 'home.html')

def current_user(request):
    cur_user = request.user
    return JsonResponse({'username': cur_user.username})

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
    form = LoginForm(request, request.POST)
    login_form = LoginForm()
    if form.is_valid():
        username = request.POST.get('username')
        password = request.POST.get('password')
        remember_me = request.POST.get('remember_me')
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            if not remember_me:
                request.session.set_expiry(0)
                request.session.modified = True
            return redirect('/library')
    return render(request, 'authentication/index.html',
                  {'login_form': login_form, 'register_form': form, 'type': 'login'})


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


@login_required
def edit_profile(request):
    user_form = EditUserForm(request.POST, instance=request.user)

    if user_form.is_valid():
        user_form.save()
        return redirect('profile')

    return render(request, 'authentication/profile.html', {'user_form': user_form})


@login_required
def view_profile(request):
    if request.method == 'POST':
        pass
    else:
        return render(request, 'authentication/profile.html', {'user': request.user})
