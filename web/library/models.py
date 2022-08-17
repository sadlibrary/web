from django.db import models
from django.contrib.auth.models import User



class LibraryTypes(models.Model):
    type = models.CharField(max_length=256, unique=True)
    formats = models.CharField(max_length=1024, blank=True)

    accepted_attachments_ids = models.CharField(max_length=1024, blank=True)


class Library(models.Model):
    owner = models.ForeignKey(User, related_name='libraries', on_delete=models.CASCADE)

    name = models.CharField(max_length=256)
    description = models.TextField()
    icon = models.ImageField(upload_to='library/icons/')
    type = models.ForeignKey(LibraryTypes, on_delete=models.RESTRICT)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class LibraryFile(models.Model):
    library = models.ForeignKey(Library, related_name='files', on_delete=models.CASCADE)
    file = models.FileField(upload_to='library/files/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    allowed_users = models.ManyToManyField(User, related_name='allowed_users')

    def __str__(self):
        return self.file.name


class FileAttachment(models.Model):
    file = models.ForeignKey(LibraryFile, related_name='attachments', on_delete=models.CASCADE)
    attachment = models.FileField(upload_to='library/attachments/')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.attachment.name
