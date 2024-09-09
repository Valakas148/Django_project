from django.db import models

from rest_framework.exceptions import PermissionDenied

from apps.subscription.choices.subs_type_choices import SubsTypeChoices


class QuerySetManager(models.QuerySet):
    pass


class CarBrandManager(models.Manager):
    def get_queryset(self):
        return QuerySetManager(self.model)


class CarManager(models.Manager):
    def get_queryset(self):
        return QuerySetManager(self.model)

