from django.contrib.auth import get_user_model
from django.db import models
from django.utils import timezone

from core.models import BaseModel

from apps.subscription.choices.subs_type_choices import SubsTypeChoices

UserModel = get_user_model()
# Create your models here.


class SubscriptionModel(models.Model):
    class Meta:
        db_table = 'subscription'
        ordering = ['-start_date']

    user = models.OneToOneField(UserModel, on_delete=models.CASCADE, related_name='subscription')
    subscription_type = models.CharField(max_length=10, choices=SubsTypeChoices.choices, default=SubsTypeChoices.BASIC)
    start_date = models.DateTimeField(default=timezone.now)
    end_date = models.DateTimeField(null=True, blank=True)

    def is_active(self):
        return self.subscription_type == SubsTypeChoices.PREMIUM and (self.end_date is None or self.end_date > timezone.now())