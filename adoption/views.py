from django.shortcuts import render,HttpResponse,redirect

# Create your views here.
def HomePage(request):
    return render(request,'home.html')

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