from django.utils import timezone

from apps.subscription.choices.subs_type_choices import SubsTypeChoices
from apps.subscription.models import SubscriptionModel

# def create_update_subscription(user, subscription_type):
#     subscription, created = SubscriptionModel.objects.get_or_create(user=user)
#     subscription.subscription_type = subscription_type
#     if subscription == SubsTypeChoices.PREMIUM:
#         subscription.start_date = timezone.now()
#         subscription.end_date = timezone.now() + timezone.timedelta(days=30)
#     else:
#         subscription.end_date = None
#     subscription.save()
#     return subscription
