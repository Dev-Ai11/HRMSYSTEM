from django.shortcuts import redirect, render, HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from website.form import SignUpForm, AddRecordForm
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
            messages.error(
                request,
                "Please read the Instructions Carefully before filling the Registration Form",
            )
            return redirect('register')
    else:
        form = SignUpForm()
        return render (request, 'register.html', {'form':form})

def show_record(request,pk):
    if request.user.is_authenticated:
        # look up records
        show_record = Record.objects.get(id=pk)

        return render(request, "show_record.html", {"show_record": show_record})
    else:
        messages.success(request, "you must logged in")
        return redirect('home')


def delete_record(request,pk):
    if request.user.is_authenticated:
        delete_it = Record.objects.get(id=pk)
        delete_it.delete()
        messages.success(request, "Record deleted successfully")
        return redirect("home")
    else:
        messages.success(request, "you must logged in")
        return redirect("home")
    

def add_record(request):
    form = AddRecordForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
             add_record = form.save()
             messages.success(request, "Record has been added")
             return redirect('home')   
    return render(request, 'add_record.html', {})

def update_record(request, pk):
    if request.user.is_authenticated:
        current_record = Record.objects.get(id=pk)
        form = AddRecordForm(request.POST or None, instance = current_record)
        if form.is_valid():
            form.save()
            messages.success(request, "Record has been updated")
            return redirect('home')
        return render(request, 'update_record.html', {'form':form} )
    else:
        messages.success(request, "you Must be logged in ..")
        return redirect('home')        
