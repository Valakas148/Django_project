from django.db import models

from core.models import BaseModel

from apps.cars.choices.body_type_choices import BodyTypeChoices
from apps.cars.managers import CarManager

# Create your models here.


class CarModel(BaseModel):
    class Meta:
        db_table = 'cars'
        ordering = ('-id',)

    brand = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    price = models.IntegerField()
    year = models.IntegerField()
    body_type = models.CharField(max_length=10, choices=BodyTypeChoices.choices)

    objects = CarManager()

