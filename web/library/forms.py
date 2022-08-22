from django import forms
from library.models import *

class TypeForm(forms.ModelForm):
    name = models.CharField(max_length=256)
    formats = models.TextField()
    accepted_attachments_ids = models.TextField()
    
    class Meta:
        model = Library
        fields = ['name', 'formats', 'accepted_attachments_ids']