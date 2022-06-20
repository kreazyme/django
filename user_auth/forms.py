from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404

class CreateUserForm(UserCreationForm):
    username = forms.CharField(max_length=256, required=True, widget=forms.TextInput(attrs={
        'class': 'form-control',
    }))

    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'class': 'form-control',
    }))

    firstname = forms.CharField(max_length=256, required=True, widget=forms.TextInput(attrs={
        'class': 'form-control',
    }))

    lastname = forms.CharField(max_length=256, required=True, widget=forms.TextInput(attrs={
        'class': 'form-control',
    }))

    password1 = forms.CharField(max_length=256, required=True, widget=forms.PasswordInput(attrs={
        'class': 'form-control',
    }))

    password2 = forms.CharField(max_length=256, required=True, widget=forms.PasswordInput(attrs={
        'class': 'form-control',
    }))

    def get_user(username):
        return get_object_or_404(User, username)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'firstname', 'lastname']
