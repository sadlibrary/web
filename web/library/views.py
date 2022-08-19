from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def check_download_permission(request, target_file):
    if request.user in target_file.allowed_user:
        return target_file
    else:
        return None