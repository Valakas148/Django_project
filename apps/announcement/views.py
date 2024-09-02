from django.shortcuts import render

from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated

from apps.announcement.models import Announcement
from apps.announcement.serializer import AnnouncementSerializer

# Create your views here.


class AnnouncementCreateListView(ListCreateAPIView):
    serializer_class = AnnouncementSerializer
    queryset = Announcement.objects.all()
    permission_classes = (IsAuthenticated,)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class AnnouncementViewUpdateDelete(RetrieveUpdateDestroyAPIView):
    serializer_class = AnnouncementSerializer
    queryset = Announcement.objects.all()
    permission_classes = (IsAuthenticated,)

