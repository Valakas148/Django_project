from django.shortcuts import render

from rest_framework.exceptions import NotFound
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated

from apps.subscription.models import SubscriptionModel
from apps.subscription.serializer import SubscriptionSerializer

# Create your views here.


class SubscriptionCreateListView(ListCreateAPIView):
    serializer_class = SubscriptionSerializer
    # queryset = SubscriptionModel.objects.all()
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        return SubscriptionModel.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class SubscriptionListUpdateDeleteView(RetrieveUpdateDestroyAPIView):
    serializer_class = SubscriptionSerializer
    queryset = SubscriptionModel.objects.all()
    permission_classes = (IsAuthenticated,)

    def get_object(self):
        user = self.request.user

        try:
            return SubscriptionModel.objects.get(user=user)
        except SubscriptionModel.DoesNotExist:
            raise NotFound('Not Found Subscription for this User')
