# views.py
from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Create your views here.
def HomePage(request):
    return render(request, 'home.html')

def LoginP(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # Store user's authentication status in session
            request.session['user_authenticated'] = True
            next_url = request.GET.get('next', 'home')
            return redirect(next_url)
        else:
            messages.info(request, "Username or Password is incorrect!!!")
            return render(request, 'home.html', {'display_alert': True})
    return render(request, 'home.html')

def RegisterP(request):
    if request.method == 'POST':
        uname = request.POST.get('username')
        email = request.POST.get('email')
        pass1 = request.POST.get('password1')
        pass2 = request.POST.get('password2')

        if User.objects.filter(username=uname).exists():
            messages.info(request, "Username already exists")
            return render(request, 'home.html', {'display_alert': True})

        if pass1 != pass2:
            messages.info(request, "Both passwords are different")
            return render(request, 'home.html', {'display_alert': True})
        else:
            my_user = User.objects.create_user(uname, email)
            my_user.set_password(pass1)
            my_user.save()
            next_url = request.GET.get('next', 'home')
            return redirect(next_url)
    return render(request, 'home.html')

def LogoutPage(request):
    logout(request)
    return redirect('home')

def FindPet(request):
    return render(request,'find_a_pet.html')

def RehomePet(request):
    return render(request,'rehome_a_pet.html')

def About(request):
    return render(request,'about_us.html')

def Donate(request):
    return render(request,'donate_us.html')

def MyAccount(request):
    return render(request,'my_account.html')
