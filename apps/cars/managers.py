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

    # def create_car(self, user, **kwargs):
    #     user_subs = user.subscription
    #     if user_subs.subscription_type == SubsTypeChoices.BASIC:
    #         if user.cars.count() >= 1:
    #             raise PermissionDenied("BASIC allows only one car to post")
    #
    #     car = self.model(user=user, **kwargs)
    #     car.save()
    #     return car

