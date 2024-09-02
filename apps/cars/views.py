from django.shortcuts import render

from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import AllowAny

from apps.cars.models import CarModel
from apps.cars.serializer import CarSerializer

# Create your views here.


class CarCreateListView(ListCreateAPIView):
    """
    Get all cars and create
    """
    serializer_class = CarSerializer
    queryset = CarModel.objects.all()
    permission_classes = (AllowAny,)


class CarViewUpdateDelete(RetrieveUpdateDestroyAPIView):
    serializer_class = CarSerializer
    queryset = CarModel.objects.all()
    permission_classes = (AllowAny,)

