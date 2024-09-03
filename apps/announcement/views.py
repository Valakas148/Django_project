from django.shortcuts import render

from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated

from apps.announcement.models import Announcement
from apps.announcement.serializer import AnnouncementSerializer
from core.services.currency_service import update_prices
# Create your views here.


class AnnouncementCreateListView(ListCreateAPIView):
    serializer_class = AnnouncementSerializer
    queryset = Announcement.objects.all()
    permission_classes = (IsAuthenticated,)

    # def perform_create(self, serializer):
    #     announcement = serializer.save(user=self.request.user)
    #     update_prices(announcement)
    #     announcement.check_lang()
    #     announcement.update_status('active' if announcement.status == 'pending' else 'inactive')
    #     serializer.save(user=self.request.user)

    def perform_create(self, serializer):
        announcement = serializer.save(user=self.request.user)
        update_prices(announcement)
        announcement.save()


class AnnouncementViewUpdateDelete(RetrieveUpdateDestroyAPIView):
    serializer_class = AnnouncementSerializer
    queryset = Announcement.objects.all()
    permission_classes = (IsAuthenticated,)

    def get_object(self):
        announcement = super().get_object()
        Announcement.objects.update_view_count(announcement.id)
        return announcement

