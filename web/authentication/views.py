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


def login(request):
    pass


def register(request):
    form = RegisterForm(request.POST)
    if form.is_valid():
        form.save()
        return redirect(to='file-manager-login')