from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm


class LoginForm(AuthenticationForm):
    username = forms.CharField(
        max_length=100,
        required=True,
        label="",
        widget=forms.TextInput(
            attrs={'placeholder': 'Username'}
        ))

    password = forms.CharField(
        max_length=50,
        required=True,
        label="",
        widget=forms.PasswordInput(
            attrs={'placeholder': 'Password'}
        ))

    remember_me = forms.BooleanField(required=False)

    class Meta:
        model = User
        fields = ['username', 'password', 'remember_me']
