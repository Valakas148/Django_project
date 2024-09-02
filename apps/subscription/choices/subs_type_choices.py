from django.db import models


class SubsTypeChoices(models.TextChoices):
    BASIC = 'basic'
    PREMIUM = 'premium'

