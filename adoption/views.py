from django.shortcuts import render,HttpResponse,redirect

# Create your views here.
def landing_page(request):
    return render(request,'index.html')