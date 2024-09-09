from django.urls import path

from apps.subscription.views import BuyPremiumSubscription, SubscriptionCreateListView, SubscriptionListUpdateDeleteView

urlpatterns = [
    path('', SubscriptionCreateListView.as_view()),
    path('/put', SubscriptionListUpdateDeleteView.as_view()),
    path('/buy-premium', BuyPremiumSubscription.as_view()),
]

