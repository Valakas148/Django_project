from django.shortcuts import render

from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated

from apps.cardealership.models import CarDealership
from apps.cardealership.serializer import CarDealershipSerializer
from apps.employees_dealership.models import DealershipEmployee

# Create your views here.


class CarDealershipListCreateView(ListCreateAPIView):
    queryset = CarDealership.objects.all()
    serializer_class = CarDealershipSerializer
    permission_classes = [IsAuthenticated,]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class CarDealershipDetailView(RetrieveUpdateDestroyAPIView):
    queryset = CarDealership.objects.all()
    serializer_class = CarDealershipSerializer
    permission_classes = [IsAuthenticated,]

