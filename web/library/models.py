from enum import unique
from django.db import models
from django.dispatch import receiver
from django.core.exceptions import ValidationError
import os


class LibraryTypes(models.Model):
    name = models.CharField(max_length=256, unique=True)
    formats = models.CharField(max_length=1024, blank=True)

    accepted_attachments_ids = models.CharField(max_length=1024, blank=True)

    def __str__(self):
        return self.name + ' (' + self.formats + ')'


class Library(models.Model):
    owner = models.ForeignKey(
        'auth.User', related_name='libraries', on_delete=models.CASCADE)

    name = models.CharField(max_length=256)
    description = models.TextField()
    library_type = models.ForeignKey(LibraryTypes, on_delete=models.RESTRICT)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ('owner', 'name')

    def __str__(self):
        return self.name


class LibraryFile(models.Model):
    library = models.ForeignKey(
        Library, related_name='files', on_delete=models.CASCADE)
    file = models.FileField(upload_to='library/files/')
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.file.name

    def file_name(self):
        return os.path.basename(self.file.name)


@receiver(models.signals.post_delete, sender=LibraryFile)
def auto_delete_file_on_delete(sender, instance, **kwargs):
    if instance.file:
        if os.path.isfile(instance.file.path):
            os.remove(instance.file.path)


class FileAttachment(models.Model):
    file = models.ForeignKey(
        LibraryFile, related_name='attachments', on_delete=models.CASCADE)
    attachment = models.FileField(upload_to='library/attachments/')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.attachment.name

    def filename(self):
        return os.path.basename(self.attachment.name)
