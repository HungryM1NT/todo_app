from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse
from django.contrib import auth
from django.contrib.auth.decorators import login_required

from app.forms import UserLoginForm, UserRegistrationForm, NoteAddForm
from app.models import Note


def index(request):
    login_form = UserLoginForm()
    registration_form = UserRegistrationForm()
    note_form = NoteAddForm()
    context = {
        'login_form': login_form,
        'registration_form': registration_form,
        'note_form': note_form,
    }
    if request.user.is_authenticated:
        context['notes'] = Note.objects.filter(user=request.user)
    return render(request, 'app/index.html', context)


def login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user:
                auth.login(request, user)
    return HttpResponseRedirect(reverse('index'))


def registration(request):
    if request.method == 'POST':
        form = UserRegistrationForm(data=request.POST)
        if form.is_valid():
            form.save()
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
def delete_note(request, note_id):
    note = Note.objects.get(id=note_id)
    note.delete()
    return HttpResponseRedirect(request.META['HTTP_REFERER'])