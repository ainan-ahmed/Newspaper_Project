from django.db import models
from django.contrib.auth.models import AbstractUser,AbstractBaseUser
# Create your models here.
class CustomUser(AbstractUser):
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )
    date_of_birth = models.DateField(null = True, blank = True)