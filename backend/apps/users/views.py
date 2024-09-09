from django.contrib.auth import get_user_model
from django.shortcuts import render

from rest_framework import status
from rest_framework.generics import (
    DestroyAPIView,
    GenericAPIView,
    ListCreateAPIView,
    RetrieveAPIView,
    RetrieveUpdateDestroyAPIView,
    UpdateAPIView,
)
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from core.permissions.is_admin_or_write_only import IsAdminOrWriteOnly
from core.permissions.is_super_user_or_manager_permission import IsSuperUserOrManagerPermission
from core.permissions.is_super_user_permission import IsSuperUserPermission

from apps.users.serializer import UserSerializer

# Create your views here.

UserModel = get_user_model()


class UserListCreateView(ListCreateAPIView):
    # permission_classes = [IsAdminOrWriteOnly,]
    permission_classes = [AllowAny,]
    serializer_class = UserSerializer
    queryset = UserModel.objects.all()


class UserUpdateDestroyView(UpdateAPIView, DestroyAPIView):
    permission_classes = [IsSuperUserOrManagerPermission,]
    serializer_class = UserSerializer
    queryset = UserModel.objects.all()


class UserRetrieveView(RetrieveAPIView):
    permission_classes = [AllowAny,]
    serializer_class = UserSerializer
    queryset = UserModel.objects.all()


class UserBlockView(GenericAPIView):
    permission_classes = (IsSuperUserOrManagerPermission,)

    def get_queryset(self):
        return UserModel.objects.exclude(pk=self.request.user.pk)

    def patch(self, request, *args, **kwargs):
        user = self.get_object()

        if user.is_active:
            user.is_active = False
            user.save()

        serializer = UserSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)


class UserUnBlockView(GenericAPIView):
    permission_classes = (IsSuperUserOrManagerPermission,)

    def get_queryset(self):
        return UserModel.objects.exclude(pk=self.request.user.pk)

    def patch(self, request, *args, **kwargs):
        user = self.get_object()

        if not user.is_active:
            user.is_active = True
            user.save()

        serializer = UserSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)


class UserToAdminView(GenericAPIView):
    """
    Цей клас де адмін робить інших адмінів
    Ака замовник та його партнери
    """
    permission_classes = (IsSuperUserPermission,)

    def get_queryset(self):
        return UserModel.objects.exclude(pk=self.request.user.pk)

    def patch(self, request, *args, **kwargs):
        user = self.get_object()

        if not user.is_staff and not user.is_manager and not user.is_superuser:
            user.is_staff = True
            user.is_manager = True
            user.is_superuser = True
            user.is_seller = False

            user.save()

        serializer = UserSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)


class UserToManagerView(GenericAPIView):
    """
    Це клас де адмін робить менеджерів
    """
    permission_classes = (IsSuperUserPermission,)

    def get_queryset(self):
        return UserModel.objects.exclude(pk=self.request.user.pk)

    def patch(self, request, *args, **kwargs):
        user = self.get_object()

        if not user.is_staff and not user.is_manager:
            user.is_staff = True
            user.is_manager = True
            user.is_seller = False

            user.save()

        serializer = UserSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)
