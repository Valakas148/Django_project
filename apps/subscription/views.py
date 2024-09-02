from django.shortcuts import render

from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated

from apps.subscription.models import SubscriptionModel
from apps.subscription.serializer import SubscriptionSerializer

# Create your views here.


class SubscriptionCreateListView(ListCreateAPIView):
    serializer_class = SubscriptionSerializer
    queryset = SubscriptionModel.objects.all()
    permission_classes = (IsAuthenticated,)


class SubscriptionListUpdateDeleteView(RetrieveUpdateDestroyAPIView):
    serializer_class = SubscriptionSerializer
    queryset = SubscriptionModel.objects.all()
    permission_classes = (IsAuthenticated,)
