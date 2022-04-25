from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager, User

class UserProfileManager(BaseUserManager):
    """ Manager for user profile """
    
    def create_user(self, email, name, password=None):
        """ Create new user Profile"""
        if not email:
            raise ValueError('El usuario debe de tener un correo')

        email = self.normalize_email(email)
        user = self.model(email=email, name=name)

        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, name, password):
        user = self.create_user(email, name, password)

        user.is_superuser = True
        user.is_staff = True

        user.save(using=self._db)
    

class UserProfile(AbstractBaseUser, PermissionsMixin):
    """ User model DB for users"""
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    object =  UserProfileManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def get_full_name(self):
        """ Get user full name """
        return self.name

    def get_short_name(self):
        """ Get user short name"""
        return self.name

    def __str__(self):
        """ return string represent our user """
        return self.email