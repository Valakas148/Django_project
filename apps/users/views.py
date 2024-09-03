from django.contrib.auth import get_user_model
from django.shortcuts import render

from rest_framework import status
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from core.permissions.is_admin_or_write_only import IsAdminOrWriteOnly
from core.permissions.is_super_user_or_manager_permission import IsSuperUserOrManagerPermission

from apps.users.serializer import UserSerializer

# Create your views here.

UserModel = get_user_model()


class UserListCreateView(ListCreateAPIView):
    permission_classes = [IsAdminOrWriteOnly,]
    serializer_class = UserSerializer
    queryset = UserModel.objects.all()


class UserRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsSuperUserOrManagerPermission,]
    serializer_class = UserSerializer
    queryset = UserModel.objects.all()

    def perform_destroy(self, instance):
        instance.delete()
        return Response({"detail": "User has been deleted"}, status=status.HTTP_200_OK)
