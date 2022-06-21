from getpass import getuser
from typing_extensions import Required
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth import authenticate, login, logout
from matplotlib.style import use
from requests import request
from django.contrib.auth.models import User

import user_auth
from .forms import CreateUserForm, UpdateUserForm

# Create your views here.


def register_account(req):
    if req.user.is_authenticated:
        return redirect('books:home')

    form = CreateUserForm()

    if req.method == 'POST':
        form = CreateUserForm(req.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            return redirect('user_auth:login')

    context = {
        'form': form,
    }

    return render(req, 'registration/register.html', context)


def login_account(req):
    if req.user.is_authenticated:
        return redirect('books:home')

    if req.method == 'POST':
        username = req.POST.get('username')
        password = req.POST.get('password')
        user = authenticate(username=username, password=password)

        if user is not None:
            login(req, user)
            return redirect('books:home')

    context = {}
    return render(req, 'registration/login.html', context)


def edit_account(req):
    user = get_object_or_404(User, username = req.user)
    userform = UpdateUserForm(req.POST or None, instance = user)

    if req.method == 'POST':
        if userform.is_valid:
            userform.save()
            return redirect('books:home')
        else:
            print("Sai form")
            return redirect('books:home')
    context = {
        'form': userform,
        'user': user,
    }
    return render(req, 'registration/edit_user.html', context)

def logout_account(req):
    logout(req)
    return redirect('user_auth:login')
