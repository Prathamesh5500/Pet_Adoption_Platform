from django.contrib import admin
from django.urls import path
from adoption import views

urlpatterns = [
    path('',views.landing_page,name="langing_page")
]
