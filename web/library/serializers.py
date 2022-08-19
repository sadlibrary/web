from rest_framework import serializers
from library.models import LibraryFile

class FileSerializer(serializers.ModelSerializer):
    class Meta:
        model = LibraryFile
        fields = ['library', 'file', 'created_at', 'updated_at']