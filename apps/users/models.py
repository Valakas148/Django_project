from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.core import validators as V
from django.db import models
from django.utils.translation import gettext_lazy as _

from core.enums.regex_enum import RegexEnum
from core.models import BaseModel

from apps.users.managers import UserManager

# Create your models here.


class UserModel(AbstractBaseUser, PermissionsMixin, BaseModel):
    class Meta:
        db_table = 'users'
        ordering = ['id']

    email = models.EmailField(unique=True)
    password = models.CharField(_("password"), max_length=128,
                                validators=(V.RegexValidator(*RegexEnum.PASSWORD.value),))
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    # is_buyer = models.BooleanField(default=False)
    is_seller = models.BooleanField(default=False)
    is_manager = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    USERNAME_FIELD = 'email'
    objects = UserManager()

    def save(self, *args, **kwargs):
        if not self.is_seller and not self.is_manager and not self.is_admin:
             self.is_seller = True
        super().save(*args, **kwargs)


class UserProfileModel(BaseModel):
    class Meta:
        db_table = 'profile'
        ordering = ['id']

    name = models.CharField(max_length=20,
                            validators=(V.RegexValidator(*RegexEnum.NAME.value),))
    surname = models.CharField(max_length=20,
                               validators=(V.RegexValidator(*RegexEnum.NAME.value),))
    age = models.IntegerField()
    user = models.OneToOneField(UserModel, on_delete=models.CASCADE, related_name='profile')
    phone_number = models.CharField(max_length=10)

