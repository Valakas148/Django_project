from django.contrib.auth import get_user_model
from django.db import models

from core.models import BaseModel

from apps.announcement.choices.status_type_choices import StatusTypeChoices
from apps.cars.models import CarModel

# Create your models here.
UserModel = get_user_model()


class Announcement(BaseModel):
    class Meta:
        db_table = 'announcements'
        ordering = ('-id',)

    user = models.ForeignKey(UserModel, on_delete=models.CASCADE, related_name='announcements')
    car = models.ForeignKey(CarModel, on_delete=models.CASCADE, related_name='announcements')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    place = models.CharField(max_length=100)
    description = models.TextField()
    status = models.CharField(max_length=20, choices=StatusTypeChoices, default='pending')