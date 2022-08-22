from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from rest_framework import viewsets, permissions
from library.models import Library
from library.serializers import LibrarySerializer


class LibraryViewSet(viewsets.ModelViewSet):
    queryset = Library.objects.all()
    serializer_class = LibrarySerializer
<<<<<<< HEAD
    # permission_classes = [permissions.IsAuthenticated]
=======
    permission_classes = [permissions.IsAuthenticated]

@login_required
def library_home(request):
    return render(request, 'base.html')
>>>>>>> 2db4185098a4cd90557400a20a75b789a04a1c5b
