from django.contrib.auth import get_user_model
from django.db import models

from core.models import BaseModel

# Create your models here.
UserModel = get_user_model()


class CarDealership(BaseModel):
    class Meta:
        db_table = 'car_dealership'
        ordering = ('-id',)
    name = models.CharField(max_length=100)
    place = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=10)
    email = models.EmailField()
    owner = models.ForeignKey(UserModel, on_delete=models.CASCADE, related_name='owned_dealerships')
