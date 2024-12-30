from django.contrib import messages
from django.shortcuts import render, redirect
from django.urls import reverse

from userauths.forms import UserRegistrationForm, UserLoginForm
from django.contrib.auth import login, authenticate, logout

from userauths.models import User


# Create your views here.

def register(request):
    if request.user.is_authenticated:
        return redirect(reverse('core:index'))
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST or None)
        if form.is_valid():
            new_user = form.save()
            username = form.cleaned_data.get("username")
            messages.success(request, f"New Account Created Successfully: {username}")
            new_user = authenticate(username=form.cleaned_data['email'], password=form.cleaned_data['password1'])
            login(request, new_user)
            return redirect(reverse('core:index'))
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"Error in {field}: {error}")
    else:
        form = UserRegistrationForm()

    context = {
        'form': form,
    }
    return render(request, 'authentication/register.html', context)


def loggin(request):
    if request.user.is_authenticated:
        return redirect(reverse('core:index'))

    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            user = authenticate(request, email=email, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f"Welcome back {user.username}")
                return redirect(reverse('core:index'))
            else:
                if not User.objects.filter(email=email).exists():
                    messages.error(request, 'Invalid email')
                else:
                    messages.error(request, 'Invalid password')
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"Error in {field}: {error}")
    else:
        form = UserLoginForm()

    context = {
        'form': form,
    }
    return render(request, 'authentication/login.html', context)


def loggout(request):
    logout(request)
    messages.error(request, 'You have been logged out')
    return redirect(reverse('userauths:login'))
