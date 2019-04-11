from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User


class UserProfileInfo(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    profile_pic = models.ImageField(upload_to='profile_pics',blank=True,default='invalid.jpg')

    def __str__(self):
        return self.user.username
class UserScore(models.Model):
    username = models.CharField(max_length=20,unique=True)
    score1 = models.IntegerField(default=0)
    score2 = models.IntegerField(default=0)
    score3 = models.IntegerField(default=0)
    score4 = models.IntegerField(default=0)
    score5 = models.IntegerField(default=0)
    score6 = models.IntegerField(default=0)
    score7 = models.IntegerField(default=0)
    score8 = models.IntegerField(default=0)
    score9 = models.IntegerField(default=0)
    score10 = models.IntegerField(default=0)
    score11 = models.IntegerField(default=0)
    score12 = models.IntegerField(default=0)
    score13 = models.IntegerField(default=0)
    score14 = models.IntegerField(default=0)
    score15 = models.IntegerField(default=0)
    totalScore = models.IntegerField(default=0)
    attended1= models.CharField(max_length=5,default="False")
    attended2= models.CharField(max_length=5,default="False")
    attended3= models.CharField(max_length=5,default="False")
    attended4= models.CharField(max_length=5,default="False")
    attended5= models.CharField(max_length=5,default="False")
    attended6= models.CharField(max_length=5,default="False")
    attended7= models.CharField(max_length=5,default="False")
    attended8= models.CharField(max_length=5,default="False")
    attended9= models.CharField(max_length=5,default="False")
    attended10= models.CharField(max_length=5,default="False")
    attended11= models.CharField(max_length=5,default="False")
    attended12= models.CharField(max_length=5,default="False")
    attended13= models.CharField(max_length=5,default="False")
    attended14= models.CharField(max_length=5,default="False")
    attended15= models.CharField(max_length=5,default="False")
    def __str__(self):
        return self.username 

class Videos(models.Model):
    name = models.CharField(max_length = 20)
    video = models.FileField(upload_to="tuturials",null=True)
    def __str__(self):
        return self.name + ":" + str(self.video)
