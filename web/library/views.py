from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from rest_framework import viewsets, permissions
from library.models import Library
from library.serializers import LibrarySerializer
from library.forms import LibraryForm, TypeForm
from django.shortcuts import render, redirect


class LibraryViewSet(viewsets.ModelViewSet):
    queryset = Library.objects.all()
    serializer_class = LibrarySerializer
    permission_classes = [permissions.IsAuthenticated]


@login_required
def library_home(request):
    type_form = TypeForm()
    library_form = LibraryForm()
    user_libraries = get_user_libraries(request)
    return render(request, 'base.html', {'type_form': type_form, 'library_form': library_form, 'user_libraries': user_libraries})


@login_required
def add_library_type(request):
    if request.method == 'POST':
        form = TypeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/library')
    type_form = TypeForm()
    return render(request, 'base.html', {'type_form': type_form})

@login_required
def add_library(request):
    if request.method == 'POST':
        form = LibraryForm(request.POST)
        if form.is_valid():
            new_library = form.save(commit=False)
            new_library.owner = request.user
            new_library.save()
            form.save_m2m()
            return redirect('/library')
    library_form = LibraryForm()
    return render(request, 'base.html', {'library_form': library_form})


@login_required
def get_user_libraries(request):
    user_libraries = Library.objects.all().filter(owner=request.user)
    return user_libraries

@login_required
def delete_library(request):
    Library.objects.all().filter(name=request.POST['library_to_delete']).delete()
    return redirect('/library')