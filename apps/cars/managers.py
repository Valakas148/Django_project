from django.db import models


class QuerySetManager(models.QuerySet):
    pass


class CarManager(models.Manager):
    def get_queryset(self):
        return QuerySetManager(self.model)