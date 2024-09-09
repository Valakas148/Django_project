
from django.db import models


class StatusTypeChoices(models.TextChoices):
    Active = "Active"
    Inactive = "Inactive"
    Pending = "Pending"

