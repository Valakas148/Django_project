from django.db import models


class EmployeeRoleChoices(models.TextChoices):
    ADMIN = 'admin', 'Administrator'
    MANAGER = 'manager', 'Manager'
    SALESPERSON = 'salesperson', 'Salesperson'
    MECHANIC = 'mechanic', 'Mechanic'