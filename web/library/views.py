from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from rest_framework import viewsets, permissions
from library.models import Library
from library.serializers import LibrarySerializer
from library.forms import TypeForm
from django.shortcuts import render, redirect


class LibraryViewSet(viewsets.ModelViewSet):
    queryset = Library.objects.all()
    serializer_class = LibrarySerializer
    permission_classes = [permissions.IsAuthenticated]

@login_required
def library_home(request):
    return render(request, 'base.html')

@login_required
def add_library_type(request):
    if request.method == 'POST':
        form = TypeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/library')
    type_form = TypeForm()
    return render(request, 'authentication/index.html', {'type_form': type_form})
    