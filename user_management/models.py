from django.db import models


# Create your models here.

class User(models.Model):
    fullName = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    userName = models.EmailField(max_length=100)
    dob = models.DateTimeField()
    userType = models.CharField(max_length=100)
