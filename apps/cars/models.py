from django.contrib.auth import get_user_model
from django.db import models

from core.models import BaseModel

from apps.cars.choices.body_type_choices import BodyTypeChoices
from apps.cars.managers import CarManager

# Create your models here.
UserModel = get_user_model()


class CarModel(BaseModel):
    class Meta:
        db_table = 'cars'
        ordering = ('-id',)

    user = models.ForeignKey(UserModel, on_delete=models.CASCADE, related_name='cars')
    brand = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    price = models.IntegerField()
    year = models.IntegerField()
    body_type = models.CharField(max_length=10, choices=BodyTypeChoices.choices)

    objects = CarManager()

