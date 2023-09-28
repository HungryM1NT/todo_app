from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from app.models import User, Note


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': "Username",
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': "Password",
    }))


    class Meta:
        model = User
        fields = ['username_email', 'password']


class UserRegistrationForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': "Username",
    }))
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'placeholder': "Email",
    }))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': "Password",
    }))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': "Confirm password",
    }))

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class NoteAddForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Name'
    }))
    description = forms.CharField(widget=forms.Textarea(attrs={
        'placeholder': 'Description'
    }))

    class Meta:
        model = Note
        fields = ['name', 'description']

    def __init__(self, *args, **kwargs):
        super(NoteAddForm, self).__init__(*args, **kwargs)
        self.fields['description'].required = False