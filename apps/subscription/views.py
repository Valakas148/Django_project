from django.shortcuts import render
from django.utils import timezone

from rest_framework import status
from rest_framework.exceptions import NotFound
from rest_framework.generics import GenericAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response

from core.services.payment_service import PaymentService

from apps.subscription.choices.subs_type_choices import SubsTypeChoices
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


class BuyPremiumSubscription(GenericAPIView):
    permission_classes = (IsAuthenticated,)

    def patch(self, request, *args, **kwargs):
        user = self.request.user

        payment_service = PaymentService.fake_process_payment(user)

        if payment_service:
            subscription, created = SubscriptionModel.objects.get_or_create(user=user)
            subscription.subscription_type = SubsTypeChoices.PREMIUM
            subscription.start_date = timezone.now()
            subscription.end_date = timezone.now() + timezone.timedelta(days=30)
            subscription.save()

            return Response({"message": "Your account has been upgraded to premium!"}, status=status.HTTP_200_OK)

        else:
            return Response({"error": "Payment failed."}, status=status.HTTP_400_BAD_REQUEST)

