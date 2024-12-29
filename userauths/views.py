from django.contrib import messages
from django.shortcuts import render, redirect
from django.urls import reverse

from userauths.forms import UserRegistrationForm
from django.contrib.auth import login, authenticate
# Create your views here.

def register(request):
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
            # Print form errors to the console for debugging
            print(form.errors)
            messages.error(request, "There was an error with your submission. Please check the form and try again.")
    else:
        form = UserRegistrationForm()

    context = {
        'form': form,
    }
    return render(request, 'register.html', context)