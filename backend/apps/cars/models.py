from django.contrib.auth import get_user_model
from django.db import models

from core.models import BaseModel

from apps.cars.choices.body_type_choices import BodyTypeChoices
from apps.cars.managers import CarManager

# Create your models here.
UserModel = get_user_model()


class CarBrand(BaseModel):
    class Meta:
        db_table = 'car_brand'
        ordering = ('-id',)

    name = models.CharField(max_length=100, unique=True)


class CarModel(BaseModel):
    class Meta:
        db_table = 'cars'
        ordering = ('-id',)
        # unique_together = ('brand', 'model', 'year', 'body_type')

    brand = models.ForeignKey(CarBrand, on_delete=models.CASCADE, related_name='models')
    model = models.CharField(max_length=100)
    year = models.IntegerField()
    body_type = models.CharField(max_length=10, choices=BodyTypeChoices.choices)



