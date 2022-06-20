from getpass import getuser
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth import authenticate, login, logout
from matplotlib.style import use

import user_auth
from .forms import CreateUserForm

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
    user = req.user
    # user = getuser(username = username)
    # user = get_object_or_404(user_auth, username = username)
    form = CreateUserForm(req.POST or None,instance = user)

    if req.method == 'POST':
        form.save()
        return redirect('books:home')

    context = {
        'form': form,
        'user': user,
    }

    return render(req, 'registration/edit_user.html', context)

def logout_account(req):
    logout(req)
    return redirect('user_auth:login')
