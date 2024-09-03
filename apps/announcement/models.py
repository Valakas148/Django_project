from django.contrib.auth import get_user_model
from django.db import models

from apps.announcement.managers import AnnouncementManager
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
    price_uah = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    price_usd = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    price_eur = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)

    exchange_rate_usd = models.DecimalField(max_digits=10, decimal_places=4, help_text="USD to UAH", null=True, blank=True)
    exchange_rate_eur = models.DecimalField(max_digits=10, decimal_places=4, help_text="EUR to UAH", null=True, blank=True)
    original_currency = models.CharField(max_length=3, choices=[('USD', "USD"), ('EUR', "EUR"), ('UAH', 'UAH')])
    original_price = models.DecimalField(max_digits=10, decimal_places=2)
    place = models.CharField(max_length=100)
    description = models.TextField()
    status = models.CharField(max_length=20, choices=StatusTypeChoices, default='pending')

    view_count = models.PositiveIntegerField(default=0)
    views_last_day = models.PositiveIntegerField(default=0)
    views_last_week = models.PositiveIntegerField(default=0)
    views_last_month = models.PositiveIntegerField(default=0)

    objects = AnnouncementManager()
