from django.shortcuts import render, redirect
from .forms import RegisterForm

from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import login


# Create your views here.
def register(response):
    if response.method == "POST":
        form = RegisterForm(response.POST)
        if form.is_valid():
            form.save()
            # new_user = User.objects.create_user(**form.cleaned_data)
            # login(new_user)
            # # redirect, or however you want to get to the main view
            # return HttpResponseRedirect('main.html')
        else:
            return render(response, "register/register.html", {"message":"username exists or bad password", "form" :  RegisterForm()})
        return redirect("..")
    else:
        form = RegisterForm()

    return render(response, "register/register.html", {"form":form})