from django.shortcuts import render

from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated

from core.permissions.is_auth_or_read_only import IsAuthenticatedOrReadOnly
from core.permissions.is_manager_permission import IsManagerPermission
from core.permissions.is_super_user_or_manager_permission import IsSuperUserOrManagerPermission
from core.permissions.is_super_user_permission import IsSuperUserPermission

from apps.cars.models import CarBrand, CarModel
from apps.cars.serializer import CarBrandSerializer, CarSerializer

# Create your views here.


class CarBrandCreateListView(ListCreateAPIView):
    queryset = CarBrand.objects.all()
    serializer_class = CarBrandSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)

    def get_permissions(self):
        if self.request.method in ['POST']:
            self.permission_classes = [IsSuperUserOrManagerPermission]
        return super().get_permissions()


class CarBrandViewUpdateDelete(RetrieveUpdateDestroyAPIView):
    queryset = CarBrand.objects.all()
    serializer_class = CarBrandSerializer
    permission_classes = [IsAuthenticatedOrReadOnly,]

    def get_permissions(self):
        if self.request.method in ['PUT', 'PATCH', 'DELETE']:
            self.permission_classes = [IsSuperUserOrManagerPermission]
        return super().get_permissions()


class CarCreateListView(ListCreateAPIView):
    serializer_class = CarSerializer
    queryset = CarModel.objects.all()
    permission_classes = (IsAuthenticatedOrReadOnly,)

    def get_permissions(self):
        if self.request.method in ['POST']:
            self.permission_classes = [IsSuperUserOrManagerPermission]
        return super().get_permissions()


class CarViewUpdateDelete(RetrieveUpdateDestroyAPIView):
    serializer_class = CarSerializer
    queryset = CarModel.objects.all()
    permission_classes = (IsAuthenticatedOrReadOnly,)

    def get_permissions(self):
        if self.request.method in ['PUT', 'PATCH', 'DELETE']:
            self.permission_classes = [IsSuperUserOrManagerPermission]
        return super().get_permissions()

