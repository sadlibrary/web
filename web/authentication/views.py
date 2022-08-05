from django.shortcuts import render
from authentication.forms import *


def authenticate(request):
    if request.method == 'POST':
        pass
    form = LoginForm()
    return render(request, 'authentication/index.html', {'login_form': form})
