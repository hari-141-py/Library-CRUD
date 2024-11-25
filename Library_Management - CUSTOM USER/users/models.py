from django.db import models
from django.contrib.auth.models import AbstractUser

# Custom user definition

class CustomUser(AbstractUser):   # AbstractUser Represents User model
    address = models.CharField(max_length=20,default="")
    phone = models.IntegerField(default=0)

    is_superuser = models.BooleanField(default=False)  #admin user
    is_user = models.BooleanField(default=False)       #normal user

    def __str__(self):
        return self.username