
from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages

def login(request):
    if request.method == "POST":
        uname = request.POST['uname']
        password1 = request.POST['password']
        user = auth.authenticate(username=uname, password=password1)
        if user is not None:
            auth.login(request, user)
            return redirect("/")
        else:
            messages.info(request, "Invalid credentials")
            return redirect("/")

def logout(request):
    auth.logout(request)
    return redirect('/')