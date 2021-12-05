from django.db import models
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
# Create your models here.

class Staff(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    password = models.CharField(max_length=50)
    email = models.TextField()    
    phone_number = models.CharField(max_length=10)

    def __str__(self):
        return self.first_name
    

        
