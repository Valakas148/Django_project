from django.db import models
from django.db.models import Avg


class AnnouncementManager(models.Manager):
    def get_average_price_by_region(self, region, car_id):
        return self.filter(place=region, car_id=car_id).aggregate(avg_price=Avg('price_usd'))['avg_price']

    def average_price_in_ukraine(self, car_id):
        return self.filter(car_id=car_id).aggregate(avg_price=Avg('price_usd'))['avg_price']

    def update_view_count(self, announcement_id):
        announcement = self.get(pk=announcement_id)
        announcement.view_count += 1
        announcement.views_last_day += 1
        announcement.views_last_week += 1
        announcement.views_last_month += 1

        announcement.save()

