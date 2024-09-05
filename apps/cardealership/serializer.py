from rest_framework import serializers

from apps.cardealership.models import CarDealership


class CarDealershipSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarDealership
        fields = ('id', 'name', 'place', 'phone_number', 'email', 'owner')