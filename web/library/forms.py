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


class FileForm(forms.ModelForm):
    file = forms.FileField(widget=forms.FileInput(
        attrs={'class': 'form-control', 'id': "inputGroupFile01"}))
    description = forms.CharField(
        widget=forms.Textarea(
            attrs={'class': 'form-control',
                   'placeholder': 'Description',
                   'aria-label': 'Description', 'rows': '3'})
    )
    attachments = forms.FileField(
        required=False,
        widget=forms.ClearableFileInput(
            attrs={'class': 'form-control', 'multiple': True})
    )

    library_name = forms.CharField(
        widget=forms.HiddenInput()
    )

    class Meta:
        model = LibraryFile
        fields = ['file', 'description']

    def __init__(self, *args, **kwargs):
        super(FileForm, self).__init__(*args, **kwargs)
        self.fields['attachments'].required = False

    def clean_file(self):
        ext = os.path.splitext(self.cleaned_data['file'].name)[-1]
        valid_extensions = self.library.library_type.formats.split(',')
        if not ext.lower() in valid_extensions:
            raise ValidationError('Unsupported file extension.')
        return self.cleaned_data['file']

    def clean_attachments(self):
        attachments = self.files.getlist('attachments')
        if attachments:
            for attachment in attachments:
                ext = os.path.splitext(attachment.name)[-1]
                valid_extensions = self.library.library_type.accepted_attachments_ids.split(
                    ',')
                if not ext.lower() in valid_extensions:
                    raise ValidationError('Unsupported attachment extension.')
        return attachments


class ActiveLibraryForm(forms.Form):
    name = forms.CharField(max_length=256,
                           widget=forms.TextInput(
                               attrs={
                                   'class': 'form-control',
                                   'id': 'add-file-current-library-input'}))
