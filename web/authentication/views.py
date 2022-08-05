from django.shortcuts import render
from authentication.forms import *


def authenticate(request):
    if request.method == 'POST':
        pass
    login_form = LoginForm()
    register_form = RegisterForm()
    return render(request, 'authentication/index.html', {'login_form': login_form, 'register_form': register_form})
