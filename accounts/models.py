from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
# Create your models here.
from django.utils.translation import ugettext_lazy as _
from .managers import CustomUserManager
from random import randint


class CustomUser(AbstractUser):
    id = models.BigAutoField(primary_key=True)  
    username = None
    email = models.EmailField(_('email address'), unique=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    objects = CustomUserManager()

    def __str__(self):
        return str(self.email)

    # def save(self, *args, **kwargs):
    #     if not self.id:
    #         is_unique = False
    #         if not is_unique:
    #             id = randint(1000000000000000, 1999999999999999)
    #             is_unique = CustomUser.objects.filter(id=id).exists()
    #         self.id = id
    #     super(CustomUser, self).save()


