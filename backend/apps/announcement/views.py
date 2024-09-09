from django.shortcuts import render

from rest_framework.exceptions import PermissionDenied
from rest_framework.generics import (
    DestroyAPIView,
    ListAPIView,
    ListCreateAPIView,
    RetrieveAPIView,
    RetrieveUpdateDestroyAPIView,
    UpdateAPIView,
)
from rest_framework.permissions import AllowAny, IsAuthenticated

from core.permissions.is_auth_or_read_only import IsAuthenticatedOrReadOnly
from core.permissions.is_super_user_or_manager_permission import IsSuperUserOrManagerPermission
from core.services.currency_service import update_prices
from core.services.email_service import EmailService

from apps.announcement.models import Announcement
from apps.announcement.serializer import AnnouncementSerializer

# Create your views here.


class AnnouncementCreateListView(ListCreateAPIView):
    serializer_class = AnnouncementSerializer
    queryset = Announcement.objects.all()
    permission_classes = (IsAuthenticatedOrReadOnly,)

    def get_queryset(self):
        user = self.request.user
        return Announcement.objects.only_active_for_user(user)

    def perform_create(self, serializer):
        announcement = serializer.save(user=self.request.user)
        update_prices(announcement)
        announcement.save()


class AnnouncementViewUpdateDelete(UpdateAPIView, DestroyAPIView):
    serializer_class = AnnouncementSerializer
    queryset = Announcement.objects.all()
    permission_classes = (IsAuthenticated,)

    def perform_update(self, serializer):
        instance = self.get_object()
        serializer.save()
        if instance.edit_attempts >= 3 and instance.status == 'inactive':
            instance.status = 'inactive'
            instance.save()
            EmailService.send_email_to_manager(announcement_id=instance.id)

    def get_object(self):
        announcement = super().get_object()
        if announcement.user != self.request.user:
            raise PermissionDenied("Its not your announcement, you are not allowed to change it")
        Announcement.objects.update_view_count(announcement.id)
        return announcement


class AnnouncementViewDelete(DestroyAPIView):
    serializer_class = AnnouncementSerializer
    queryset = Announcement.objects.all()
    permission_classes = (IsSuperUserOrManagerPermission,)

    def get_queryset(self):
        return Announcement.objects.filter(status='inactive')


class AnnouncementDetailView(RetrieveAPIView):
    serializer_class = AnnouncementSerializer
    queryset = Announcement.objects.all()
    permission_classes = (AllowAny,)

    def get_object(self):
        announcement = super().get_object()
        user = self.request.user
        if announcement.status in ['inactive', 'pending'] and announcement.user != user:
            raise PermissionDenied("You don't have permission to view this announcement.")
        return announcement


class SeeDetailView(ListAPIView):
    serializer_class = AnnouncementSerializer
    permission_classes = (IsAuthenticated,)
    queryset = Announcement.objects.all()

    def get_queryset(self):
        user = self.request.user
        return Announcement.objects.filter(user=user)

