from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

class UserManager(BaseUserManager):

    def create_user(self, email, password=None, **extra_fields):
        #**extra_fields parameter makes our function a little more felxible
        #because every time we add new fields to our user it means we don't have
        #to add them here.
        """Creates and saves a new user"""
        user = self.model(email=email, **extra_fields)
        user.set_password(password) #using encryption helper function
        user.save(using=self._db) #using = self._db allows for any db

        return user

class User(AbstractBaseUser, PermissionsMixin): #inheritance from 2 classes
    """Custom user model that supports using email instead of username."""
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
