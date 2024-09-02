from rest_framework import serializers
from rest_framework.exceptions import PermissionDenied

from apps.announcement.models import Announcement
from apps.cars.models import CarBrand, CarModel
from apps.cars.serializer import CarSerializer
from apps.subscription.choices.subs_type_choices import SubsTypeChoices


class AnnouncementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Announcement
        fields = ('id', 'user', 'car', 'price', 'place', 'description', 'status', 'created_at', 'updated_at')
        read_only_fields = ('user', 'status', 'created_at', 'updated_at')

    def check_lang(self):
        pass

    def update_status(self, status):
        self.status = status
        self.save()

    def create(self, validated_data):
        car_data = validated_data.pop('car')
        brand_data = car_data.pop('brand')

        brand, created = CarBrand.objects.get_or_create(name=brand_data['name'])

        car, created = CarModel.objects.get_or_create(
            brand=brand,
            name=car_data['name'],
            year=car_data['year'],
            body_type=car_data['body_type']
        )

        announcement = Announcement.objects.create(car=car, **validated_data)
        return announcement

    def save(self, *args, **kwargs):
        user = kwargs.get('user')
        if not user:
            raise ValueError("User must be provided when saving an announcement.")

        user_subs = user.subscription
        if user_subs.subscription_type == SubsTypeChoices.BASIC:
            if user.announcements.count() >= 1:
                raise PermissionDenied("BASIC allows only one car to post")

        self.instance.user = user
        self.check_lang()
        super().save(**kwargs)
