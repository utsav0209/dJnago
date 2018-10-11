from django.db import models
#Create your models here.
from django.contrib.auth.models import User



class Follows(models.Model):
    person = models.ForeignKey(User,on_delete=models.CASCADE)
    following = models.CharField(max_length=20)