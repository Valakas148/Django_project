from django.urls import path

from apps.subscription.views import SubscriptionCreateListView, SubscriptionListUpdateDeleteView

urlpatterns = [
    path('', SubscriptionCreateListView.as_view()),
    path('/put', SubscriptionListUpdateDeleteView.as_view())
]

