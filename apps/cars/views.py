from django.shortcuts import render

from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated

from apps.cars.models import CarModel
from apps.cars.serializer import CarSerializer

# Create your views here.


class CarCreateListView(ListCreateAPIView):
    """
    Get all cars and create
    """
    serializer_class = CarSerializer
    queryset = CarModel.objects.all()
    permission_classes = (IsAuthenticated,)

    def perform_create(self, serializer):
        user = self.request.user
        serializer.instance = CarModel.objects.create_car(user=user, **serializer.validated_data)


class CarViewUpdateDelete(RetrieveUpdateDestroyAPIView):
    serializer_class = CarSerializer
    queryset = CarModel.objects.all()
    permission_classes = (IsAuthenticated,)

