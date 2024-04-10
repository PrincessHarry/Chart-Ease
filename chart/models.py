from django.db import models
from django.conf import settings
from  django.contrib.auth.models import AbstractUser

from django.contrib.auth.hashers import make_password
from django.utils import timezone
from django.contrib.auth.models import User

class User(AbstractUser):
    related_user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,  default=None, null=True, blank=True)
    
    username = models.CharField(max_length=200, unique=True )
    email = models.EmailField(unique=True)
    image = models.ImageField(upload_to='profile_image/', blank=True)
    dob = models.CharField(max_length=20)
    phone_number = models.CharField(max_length=20)
    organization_company = models.CharField(max_length=100)
    job_title = models.CharField(max_length=100) 
    terms_accepted = models.BooleanField(default=False)

    def __str__(self):
        return self.username
