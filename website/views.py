from django.shortcuts import redirect, render, HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from website.form import SignUpForm
from .models import Record


def home(request):
    records = Record.objects.all()
    if request.method=="POST":
        username = request.POST['username']
        password = request.POST['password']
        # authenticate
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "you have been logged in successfully")
            return redirect('home')
        else:
            messages.success(request, 'your credential are not correct please try again with right one  ')    
            return redirect('home')
    else:
     return render(request, 'home.html', {'records':records})


def logout_user(request):
    logout(request)
    messages.success(request, "you have been logged out successfully")
    return redirect('home')


def register_user(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            # authenticate and login page
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)

            if user is not None:
                login(request, user)
                messages.success(request, "you have been successfully Registered")
                return redirect('home')
        else:
            messages.error(request, "registration has been failed try again latter")    
            return redirect('register')
    else:
        form = SignUpForm()
        return render (request, 'register.html', {'form':form})
