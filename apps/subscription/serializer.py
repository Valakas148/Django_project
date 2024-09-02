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

    def update(self, instance, validated_data):
        instance.subscription_type = validated_data.get('subscription_type', instance.subscription_type)

        if instance.subscription_type == SubsTypeChoices.PREMIUM:
            instance.start_date = timezone.now()
            instance.end_date = timezone.now() + timezone.timedelta(days=30)
        else:
            instance.end_date = None

        instance.save()
        return instance
