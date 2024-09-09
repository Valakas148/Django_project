from rest_framework import serializers
from rest_framework.exceptions import PermissionDenied, ValidationError

from core.services.currency_service import update_prices
from core.services.language_bad_control import LanguageBadCheckService

from apps.announcement.models import Announcement
from apps.cars.models import CarBrand, CarModel
from apps.cars.serializer import CarSerializer
from apps.subscription.choices.subs_type_choices import SubsTypeChoices


class AnnouncementSerializer(serializers.ModelSerializer):
    car = serializers.PrimaryKeyRelatedField(
        queryset=CarModel.objects.all(),
        error_messages={
                      'does_not_exist': 'The selected car does not exist.',
                      }
        )
    average_price_by_region = serializers.SerializerMethodField()
    average_price_in_ukraine = serializers.SerializerMethodField()

    class Meta:
        model = Announcement
        fields = ('id', 'user', 'car', 'original_currency', 'original_price', 'price_uah', 'price_usd', 'price_eur',
                  'exchange_rate_usd', 'exchange_rate_eur', 'place', 'description', 'status','view_count',
                  'views_last_day', 'views_last_week', 'views_last_month', 'average_price_by_region', 'average_price_in_ukraine', 'created_at',
                  'updated_at', 'edit_attempts')
        read_only_fields = (
        'user', 'status', 'created_at', 'updated_at', 'price_uah', 'price_usd', 'price_eur', 'exchange_rate_usd',
        'exchange_rate_eur', 'view_count',
                  'views_last_day', 'views_last_week', 'views_last_month', 'average_price_by_region', 'average_price_in_ukraine', 'edit_attempts')

    def get_average_price_by_region(self, obj):
        user = self.context['request'].user
        if user.is_authenticated and user == obj.user and user.subscription.subscription_type == SubsTypeChoices.PREMIUM:
            return Announcement.objects.get_average_price_by_region(obj.place, obj.car.id)
        return None

    def get_average_price_in_ukraine(self, obj):
        user = self.context['request'].user
        if user.is_authenticated and user == obj.user and user.subscription.subscription_type == SubsTypeChoices.PREMIUM:
            return Announcement.objects.average_price_in_ukraine(obj.car.id)
        return None

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        user = self.context['request'].user

        if not user.is_authenticated or user != instance.user or user.subscription.subscription_type == SubsTypeChoices.BASIC:
            representation.pop('view_count', None)
            representation.pop('views_last_day', None)
            representation.pop('views_last_week', None)
            representation.pop('views_last_month', None)
            representation.pop('average_price_by_region', None)
            representation.pop('average_price_in_ukraine', None)

        return representation

    def create(self, validated_data):
        user = self.context['request'].user
        validated_data.pop('user', None)

        description = validated_data.get('description', '')
        if LanguageBadCheckService.check_language_bad(description):
            validated_data['status'] = 'pending'
        else:
            validated_data['status'] = 'active'

        user_subs = user.subscription
        if user_subs.subscription_type == SubsTypeChoices.BASIC:
            if user.announcements.count() >= 1:
                raise PermissionDenied("BASIC allows only one car to post")

        announcement = Announcement.objects.create(user=user, **validated_data)
        update_prices(announcement)
        return announcement

    def update(self, instance, validated_data):
        description = validated_data.get('description', instance.description)

        if LanguageBadCheckService.check_language_bad(description):
            instance.status = 'pending'
            instance.edit_attempts += 1
            if instance.edit_attempts >= 3:
                instance.status = 'inactive'
        else:
            instance.status = 'active'
            instance.edit_attempts = 0

        instance = super().update(instance, validated_data)
        update_prices(instance)
        return instance
