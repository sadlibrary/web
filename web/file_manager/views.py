from django.shortcuts import render
from .models import *
from .forms import *

def login(request):
    if request.method == 'POST':
        pass
    form = LoginForm()
    return render(request, 'file_manager/login.html', {'form': form})