from rest_framework import serializers

from apps.subscription.models import SubscriptionModel


class SubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubscriptionModel
        fields = ('user', 'subscription_type', 'start_date', 'end_date')

