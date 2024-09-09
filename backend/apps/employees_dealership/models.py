from django.contrib.auth import get_user_model
from django.db import models

from apps.cardealership.models import CarDealership
from apps.employees_dealership.choices.employee_role_choices import EmployeeRoleChoices

# Create your models here.
UserModel = get_user_model()


class DealershipEmployee(models.Model):
    class Meta:
        db_table = 'employee_dealership'
        ordering = ('-id',)

    user = models.ForeignKey(UserModel, on_delete=models.CASCADE, related_name='dealership_employees')
    dealership = models.ForeignKey(CarDealership, on_delete=models.CASCADE, related_name='employees')
    role = models.CharField(max_length=50, choices=EmployeeRoleChoices.choices)