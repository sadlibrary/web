from django.shortcuts import render, redirect
from .models import *
from .forms import *

def login(request):
    if request.method == 'POST':
        pass
    form = LoginForm()
    return render(request, 'authentication/login.html', {'form': form})


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(to='file-manager-login')
    form = RegisterForm()

    return render(request, 'authentication/register.html', {'form': form})