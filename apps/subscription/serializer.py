from django.utils import timezone

from rest_framework import serializers

from apps.subscription.choices.subs_type_choices import SubsTypeChoices
from apps.subscription.models import SubscriptionModel


class SubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubscriptionModel
        fields = ('user', 'subscription_type', 'start_date', 'end_date')
        read_only_fields = (
            'user', 'start_date', 'end_date'
        )

