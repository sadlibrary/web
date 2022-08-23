from django import forms
from library.models import *


class TypeForm(forms.ModelForm):
    class Meta:
        model = LibraryTypes
        fields = ['name', 'formats', 'accepted_attachments_ids']


class LibraryForm(forms.ModelForm):
    class Meta:
        model = Library
        fields = ['name', 'description', 'library_type']
