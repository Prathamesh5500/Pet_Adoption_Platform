from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class AdoptionImage(models.Model):
    name = models.CharField(max_length=255)
    image = models.URLField('')  # URL of the image on Cloudinary

class Seller(models.Model):
    sellername = models.CharField(max_length=50, primary_key=True)
    adoptionfee = models.IntegerField(default=0)
    phone = models.CharField(max_length=15)

class Details(models.Model):
    name = models.CharField(max_length=50, primary_key=True)
    gender = models.CharField(max_length=10, default='male')
    size = models.CharField(max_length=10, default='small')
    color = models.CharField(max_length=30, default='black')
    age = models.IntegerField(default=0)
    spayed = models.CharField(max_length=10, default='no')
    seller = models.ForeignKey(Seller, on_delete=models.CASCADE)
    image = models.ForeignKey(AdoptionImage, on_delete=models.SET_NULL, null=True, blank=True)  # Link to the image
def __str__(self):
        return self.name