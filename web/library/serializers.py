from rest_framework import serializers
from library.models import LibraryFile, Library

class FileSerializer(serializers.ModelSerializer):
    class Meta:
        model = LibraryFile
        fields = ['library', 'file', 'created_at', 'updated_at']

class LibrarySerializer(serializers.ModelSerializer):
    class Meta:
        model = Library
        fields = ['owner', 'name', 'description', 'icon', 'type', 'created_at', 'updated_at']