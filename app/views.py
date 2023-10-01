from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse
from django.contrib import auth
from django.contrib.auth.decorators import login_required

from app.forms import UserLoginForm, UserRegistrationForm, NoteAddForm
from app.models import Note


def index(request, note_id=None):
    if request.user.is_authenticated:
        context = {
            'notes': Note.objects.filter(user=request.user),
            'note_form': NoteAddForm(),
        }
    else:
        context = {
            'login_form': UserLoginForm(),
            'registration_form': UserRegistrationForm(),
        }
    if note_id:
        note = Note.objects.get(id=note_id)
        note_name = note.name
        note_description = note.description
        edit_note_form = NoteAddForm(initial={
            'name': note_name,
            'description': note_description,
        })
        context['edit_note_form'] = edit_note_form
        context['edit_note_id'] = note_id
    return render(request, 'app/index.html', context)


def login(request):
    if request.method == 'POST':
        login_form = UserLoginForm(data=request.POST)
        if login_form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user:
                auth.login(request, user)
        else:
            registration_form = UserRegistrationForm()
            context = {
                'login_form': login_form,
                'registration_form': registration_form
            }
            return render(request, 'app/index.html', context)
    return HttpResponseRedirect(reverse('index'))


def registration(request):
    if request.method == 'POST':
        registration_form = UserRegistrationForm(data=request.POST)
        if registration_form.is_valid():
            registration_form.save()
        else:
            login_form = UserLoginForm()
            context = {
                'login_form': login_form,
                'registration_form': registration_form
            }
            return render(request, 'app/index.html', context)
    return HttpResponseRedirect(reverse('index'))


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('index'))


@login_required
def add_note(request):
    if request.method == 'POST':
        notes = Note.objects.filter(user=request.user)
        form = NoteAddForm(data=request.POST)
        if form.is_valid():
            name = form.cleaned_data.get("name")
            description = form.cleaned_data.get("description")
            if notes.exists():
                Note.objects.create(user=request.user,
                                    number=notes.last().number + 1, name=name, description=description)
            else:
                Note.objects.create(user=request.user,
                                    number=1, name=name, description=description)
    return HttpResponseRedirect(reverse('index'))


@login_required
def edit_note(request, note_id):
    if request.method == 'POST':
        form = NoteAddForm(data=request.POST)
        if form.is_valid():
            Note.objects.filter(id=note_id).update(name=form.cleaned_data.get("name"),
                                                description=form.cleaned_data.get("description"))
    return HttpResponseRedirect(reverse('index'))


@login_required
def delete_note(request, note_id):
    if request.method == 'POST':
        note = Note.objects.get(id=note_id)
        note.delete()
    return HttpResponseRedirect(request.META['HTTP_REFERER'])

