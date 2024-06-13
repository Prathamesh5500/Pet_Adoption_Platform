# views.py
from django.shortcuts import render, HttpResponse, redirect,get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Details,Seller,AdoptionImage
import cloudinary.uploader
from django.conf import settings
# Create your views here.
def HomePage(request):
    return render(request, 'home.html')

def Rehome(request):
    cloudinary.config(
        cloud_name=settings.CLOUDINARY['CLOUD_NAME'],
        api_key=settings.CLOUDINARY['API_KEY'],
        api_secret=settings.CLOUDINARY['API_SECRET']
    )
    if request.method == 'POST':
        name = request.POST.get('name')  # Assuming you pass the name along with the image in the request
        image = request.FILES['image']
        uploaded_image = cloudinary.uploader.upload(image)
        # Assuming you want to save the name along with the image
        AdoptionImage.objects.create(name=name, image=uploaded_image['url'])
        name = request.POST.get('name')
        gender = request.POST.get('gender', 'Male') 
        size = request.POST.get('size')
        color = request.POST.get('color')
        age = request.POST.get('age')
        spayed = request.POST.get('spayed')
        sellername = request.POST.get('sellername')
        adoptionfee = request.POST.get('adoptionfee')
        phone = request.POST.get('phone')
        address = request.POST.get('address')
        seller, created = Seller.objects.get_or_create(
            sellername=sellername,
            defaults={'adoptionfee': adoptionfee, 'phone': phone}
        )
        if not created:
            seller.adoptionfee = adoptionfee
            seller.phone = phone
            seller.save()

        # Create the Details instance
        Details.objects.create(
            name=name,
            gender=gender,
            size=size,
            color=color,
            age=age,
            spayed=spayed,
            seller=seller,
            address=address
        )

        messages.success(request, 'Data added successfully!')
        return render(request, 'rehome_a_pet.html')

    return render(request, 'rehome_a_pet.html')

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

@login_required
def find_a_pet(request):
    pets = Details.objects.all()
    for pet in pets:
        try:
            pet.image = AdoptionImage.objects.get(name=pet.name)
        except AdoptionImage.DoesNotExist:
            pet.image = None
    return render(request, 'find_a_pet.html', {'pets': pets})


@login_required
def RehomePet(request):
    return render(request,'rehome_a_pet.html')

def About(request):
    return render(request,'about_us.html')

def Donate(request):
    return render(request,'donate_us.html')

def MyAccount(request):
    return render(request,'my_account.html')

def adopt(request, pet_name):
    pet = get_object_or_404(Details, name=pet_name)
    try:
        pet.image = AdoptionImage.objects.get(name=pet.name)
    except AdoptionImage.DoesNotExist:
            pet.image = None
    # Assuming you have a form for adoption/payment handling
    # Here's a basic example to render an adopt template
    return render(request, 'adopt.html', {'pet': pet})