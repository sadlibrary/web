from unittest import result
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from rest_framework import viewsets, permissions
from library.models import FileAttachment, Library, LibraryFile
from library.serializers import LibrarySerializer
from library.forms import ActiveLibraryForm, FileForm, LibraryForm, TypeForm
from django.shortcuts import render, redirect


class LibraryViewSet(viewsets.ModelViewSet):
    queryset = Library.objects.all()
    serializer_class = LibrarySerializer
    permission_classes = [permissions.IsAuthenticated]


@login_required
def library_home(request):
    type_form = TypeForm()
    library_form = LibraryForm()
    file_form = FileForm()
    active_library = ActiveLibraryForm()
    library_files = []
    user_libraries = get_user_libraries(request)
    if 'active_library' in request.session:
        library_files = list(get_library_files(request))
       
        del request.session['active_library']
    return render(request, 'base.html', {'type_form': type_form, 'library_form': library_form, 'user_libraries': user_libraries,
                                            'file_form': file_form, 'active_library': active_library, 'library_files': library_files})


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


@login_required
def show_library(request):
    form = ActiveLibraryForm(request.POST)
    if form.is_valid():
        request.session['active_library'] = form.cleaned_data['name']
        return redirect('/library')


@login_required
def get_library_files(request):
    active_library = Library.objects.all().filter(name=request.session['active_library'])[0]
    library_files = LibraryFile.objects.all().filter(library=active_library)
    return library_files


def is_extension_valid(FILES, library_type):
    file_ext = [ext[1:] for ext in library_type.formats.split(',')]
    att_ext = [ext[1:] for ext in library_type.formats.split(',')]
    result = FILES['file'].name.split('.')[-1] in file_ext
    for file_to_upload in FILES['attachments']:
        result = result and (file_to_upload.name.split('.')[-1] in att_ext)
    return result


@login_required
def add_library_files(request):
    if request.method == 'POST':
        form = FileForm(request.POST, request.FILES)
        print(request.POST)
        print(request.FILES)
        if form.is_valid():
            active_library = Library.objects.all().filter(name=request.session['active_library'])[0]
            #if is_extension_valid(request.FILES, active_library.library_type):
            new_file = form.save(commit=False)
            new_file.library = active_library
            new_file.save()
            new_attachment = FileAttachment(file=new_file, attachment=request.FILES['attachments'])
            new_attachment.save()
            form.save_m2m()
            return redirect('/library')
        print(form.errors)
    file_form = FileForm()
    return render(request, 'base.html', {'file_form': file_form})