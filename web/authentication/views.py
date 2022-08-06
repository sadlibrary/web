from django.shortcuts import render, redirect
from authentication.forms import *

BUTTON_LOGIN = 'login'
BUTTON_REGISTER = 'register'

def home(request):
    if request.method == 'POST':
        if BUTTON_LOGIN in request.POST:
            return login(request)
        elif BUTTON_REGISTER in request.POST:
            return register(request)
    login_form = LoginForm()
    register_form = RegisterForm()
    return render(request, 'authentication/index.html', {'login_form': login_form, 'register_form': register_form})

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

def register(request):
    form = RegisterForm(request.POST)
    if form.is_valid():
        form.save()
        return redirect(to='file-manager-login')

def auth_logout(request):
    logout(request)
    return redirect('/')
