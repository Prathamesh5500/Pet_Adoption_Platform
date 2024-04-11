from django.contrib import admin
from django.urls import path
from adoption import views

urlpatterns = [
    path('',views.HomePage,name='home'),
    path('find_a_pet/', views.FindPet, name='find_a_pet'),
    path('rehome_a_pet/', views.RehomePet, name='rehome_a_pet'),
    path('about/', views.About, name='about_us'),
    path('donate/', views.Donate, name='donate_us'),
    path('my_account/', views.MyAccount, name='my_account'),
    path('login/', views.LoginP, name='login'),
    path('register/', views.RegisterP, name='register'),
    path('logout/', views.LogoutPage, name='logout'),
]
