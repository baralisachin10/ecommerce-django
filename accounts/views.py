from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from . forms import LoginForm

# to register the user
def user_register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request,messages.SUCCESS,'Account created successfully')
            return redirect('/account/register/')
        else:
            messages.add_message(request,messages.ERROR,'Please verify the form fields')
            return render(request, 'accounts/register.html',{'form':form})
    context = {
        'form': UserCreationForm
    }
    return render(request,'accounts/register.html',context)

# to login the user
def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(request, username = form.cleaned_data['username'], password = form.cleaned_data['password'])
            if user is not None:
                login(request,user)
                return redirect("/products/")
            else:
                messages.add_message(request, messages.ERROR, "Please provide the correct credentials!")
                return render(request,"accounts/login.html",{'form':form})
    context = {
        'form': LoginForm
    }
    return render(request,'accounts/login.html',context)

