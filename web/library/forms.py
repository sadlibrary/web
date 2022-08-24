from unicodedata import name
from django import forms
from library.models import *


class TypeForm(forms.ModelForm):
    name = forms.CharField(
        max_length=256,
        required=True,
        widget=forms.TextInput(
            attrs={'class': 'form-control',
                   'placeholder': 'Name',
                   'aria-label': 'Name',
                   'aria-describedby': 'basic-addon21'})
    )

    formats = forms.CharField(
        max_length=1024,
        widget=forms.TextInput(
            attrs={'class': 'form-control',
                   'placeholder': 'Accepted Extensions'})
    )

    accepted_attachments_ids = forms.CharField(
        max_length=1024,
        widget=forms.TextInput(
            attrs={'class': 'form-control',
                   'placeholder': 'Accepted Extensions'})
    )

    class Meta:
        model = LibraryTypes
        fields = ['name', 'formats', 'accepted_attachments_ids']


class LibraryForm(forms.ModelForm):
    name = forms.CharField(
        max_length=256,
        required=True,
        widget=forms.TextInput(
            attrs={'class': 'form-control', 'id': 'library-name',
                   'placeholder': 'Name',
                   'aria-label': 'Name',
                   'aria-describedby': 'basic-addon11'})
    )

    description = forms.CharField(
        widget=forms.Textarea(
            attrs={'class': 'form-control',
                   'id': 'library-description',
                   'placeholder': 'Description',
                   'aria-label': 'Description', 'rows': '3'})
    )

    library_type = forms.ModelChoiceField(
        queryset=LibraryTypes.objects.all(),
        widget=forms.Select(
            attrs={'class': 'form-control', 'id': 'inputGroupSelect01'})
    )

    class Meta:
        model = Library
        fields = ['name', 'description', 'library_type']
