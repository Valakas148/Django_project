from django.db import models
from django.db.models import Avg


class AnnouncementManager(models.Manager):
    def get_average_price_by_region(self, region):
        return self.filter(place=region).aggregate(avg_price=Avg('original_price'))['avg_price']

    def average_price_in_ukraine(self):
        return self.aggregate(avg_price=Avg('original_price'))['avg_price']

    def update_view_count(self, announcement_id):
        announcement = self.get(pk=announcement_id)
        announcement.view_count += 1
        announcement.views_last_day += 1
        announcement.views_last_week += 1
        announcement.views_last_month += 1

        announcement.save()