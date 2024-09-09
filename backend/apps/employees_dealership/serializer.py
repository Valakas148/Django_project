from rest_framework import serializers

from apps.employees_dealership.models import DealershipEmployee


class DealershipEmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = DealershipEmployee
        fields = ('id', 'user', 'dealership', 'role')

