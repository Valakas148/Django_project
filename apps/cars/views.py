from django.shortcuts import render

from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated

from core.permissions.is_manager_permission import IsManagerPermission
from core.permissions.is_super_user_or_manager_permission import IsSuperUserOrManagerPermission
from core.permissions.is_super_user_permission import IsSuperUserPermission

from apps.cars.models import CarBrand, CarModel
from apps.cars.serializer import CarBrandSerializer, CarSerializer

# Create your views here.


class CarBrandCreateListView(ListCreateAPIView):
    queryset = CarBrand.objects.all()
    serializer_class = CarBrandSerializer
    permission_classes = (IsSuperUserOrManagerPermission,)


class CarBrandViewUpdateDelete(RetrieveUpdateDestroyAPIView):
    queryset = CarBrand.objects.all()
    serializer_class = CarBrandSerializer
    permission_classes = [IsSuperUserOrManagerPermission,]


class CarCreateListView(ListCreateAPIView):
    """
    Get all cars and create
    """
    serializer_class = CarSerializer
    queryset = CarModel.objects.all()
    permission_classes = (IsSuperUserOrManagerPermission,)

    # def perform_create(self, serializer):
    #     user = self.request.user
    #     serializer.instance = CarModel.objects.create_car(user=user, **serializer.validated_data)


class CarViewUpdateDelete(RetrieveUpdateDestroyAPIView):
    serializer_class = CarSerializer
    queryset = CarModel.objects.all()
    permission_classes = (IsSuperUserOrManagerPermission,)

