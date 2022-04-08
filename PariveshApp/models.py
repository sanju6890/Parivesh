from django.db import models
from django.db.models.deletion import CASCADE
from django.contrib.auth.models import User
from django.urls import reverse


# Create your models here.

class Plantation(models.Model):
    planter  = models.ForeignKey(User, on_delete=CASCADE)
    plant_name = models.CharField(max_length=255)
    plant_loc = models.URLField()
    plant_pic = models.ImageField(null=True,blank=True, upload_to='plant_pics')
    date_time = models.DateTimeField(auto_now_add=True)
    remarks = models.TextField()

    def __str__(self):
        return f'{self.plant_name} | {str(self.planter.first_name)} | ' + str(self.planter.email)
    
    def get_absolute_url(self):
        return reverse('home')

class Profile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    bio = models.TextField()
    profile_pic = models.ImageField(null=True,blank=True, upload_to="profile_pics")
    # NITJ Membership Info
    designation = models.CharField(max_length=255)
    department = models.CharField(max_length=255)
    # If Designation is Student
    roll_no = models.CharField(max_length=255,null=True,blank=True)
    degree_type = models.CharField(max_length=255,null=True,blank=True)    
    batch = models.CharField(max_length=255,null=True,blank=True) 
    # Social Links   
    website_url = models.URLField(null=True, blank=True)
    facebook_url = models.URLField(null=True, blank=True)
    instagram_url = models.URLField(null=True, blank=True)
    linkedin_url = models.URLField(null=True, blank=True)
    twitter_url = models.URLField(null=True, blank=True)

    def __str__(self):
        return str(self.user)

    def get_absolute_url(self):
        return reverse('home')