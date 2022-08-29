from unittest import result
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from rest_framework import viewsets, permissions
from library.models import FileAttachment, Library, LibraryFile
from library.serializers import LibrarySerializer
from library.forms import ActiveLibraryForm, FileForm, LibraryForm, TypeForm
from django.shortcuts import render, redirect
from django.contrib.auth.models import User


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
    attachments = []
    user_libraries = get_user_libraries(request)
    if 'active_library' in request.session:
        library_files, attachments = get_library_files(request)
        library_files = list(library_files)
    return render(request, 'base.html', {'type_form': type_form, 'library_form': library_form, 'user_libraries': user_libraries,
                                         'file_form': file_form, 'active_library': active_library, 'library_files': library_files,
                                         'attachments': attachments, 'range_file': range(len(library_files))})


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
    Library.objects.all().filter(
        name=request.POST['library_to_delete'], owner=request.user).delete()
    return redirect('/library')


@login_required
def share_library(request):
    library_to_share = Library.objects.all().filter(
        name=request.POST['library_to_share'])[0]
    library_files = LibraryFile.objects.all().filter(library=library_to_share)
    library_to_share.id = None
    user_to_share = User.objects.all().filter(
        username=request.POST['username_to_share'])[0]
    library_to_share.owner = user_to_share
    library_to_share.save()

    for original_file in library_files:
        # original_file.id = None
        # original_file.library = library_to_share
        new_file = LibraryFile(library=library_to_share,
                               file=original_file.file)
        new_file.save()
        # original_file.save()

    return redirect('/library')


@login_required
def show_library(request):
    form = ActiveLibraryForm(request.POST)
    if form.is_valid():
        request.session['active_library'] = form.cleaned_data['name']
        return redirect('/library')


@login_required
def get_library_files(request):
    active_library = Library.objects.all().filter(
        name=request.session['active_library'], owner=request.user)[0]
    library_files = LibraryFile.objects.all().filter(library=active_library)
    attachments = []
    for file in library_files:
        attachment = FileAttachment.objects.all().filter(file=file)
        if (attachment):
            attachments.append(attachment[0])
        else:
            attachments.append(None)

    return library_files, attachments


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
            active_library = Library.objects.all().filter(
                name=request.session['active_library'])[0]
            # if is_extension_valid(request.FILES, active_library.library_type):
            new_file = form.save(commit=False)
            new_file.library = active_library
            new_file.save()
            attachment = request.FILES.get('attachments')
            if attachment:
                new_attachment = FileAttachment(
                    file=new_file, attachment=attachment)
                new_attachment.save()
            form.save_m2m()
            return redirect('/library')
        print(form.errors)
    file_form = FileForm()
    return render(request, 'base.html', {'file_form': file_form})
